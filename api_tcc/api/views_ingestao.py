from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from api_tcc.models import LeituraTelemetria
from api_tcc.api.serializers import LeituraTelemetriaSerializer
from api_tcc.ia.anomalias import detectar_anomalias
from api_tcc.ia.manutencao import prever_manutencao


class AnomaliaView(APIView):
    """
    GET /api/anomalias/
    GET /api/anomalias/?maquina_id=COLH-01

    Detecta leituras fora do padrão usando Isolation Forest.
    Precisa de pelo menos 20 leituras no banco para funcionar.
    """
    def get(self, request):
        maquina = request.query_params.get('maquina_id')
        resultado = detectar_anomalias(maquina_id=maquina)
        return Response(resultado)

class IngestaoTelemetriaView(APIView):

    def post(self, request):
        uuid_recebido = request.data.get('id')
        if uuid_recebido:
            if LeituraTelemetria.objects.filter(id=uuid_recebido).exists():
                return Response(
                    {'status': 'duplicata ignorada', 'id': uuid_recebido},
                    status=status.HTTP_200_OK
                )

        serializer = LeituraTelemetriaSerializer(data=request.data)
        if serializer.is_valid():
            maquina_id = serializer.validated_data.get('maquina_id', '').strip()
            if not maquina_id:
                return Response(
                    {'status': 'erro', 'detalhes': {'maquina_id': 'Este campo não pode ser vazio.'}},
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                serializer.save()
            except IntegrityError:
                return Response(
                    {'status': 'duplicata ignorada', 'id': str(serializer.validated_data.get('id', ''))},
                    status=status.HTTP_200_OK
                )
            return Response(
                {'status': 'ok', 'id': str(serializer.data['id'])},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'status': 'erro', 'detalhes': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):
        maquina = request.query_params.get('maquina_id')
        leituras = LeituraTelemetria.objects.all()
        if maquina:
            leituras = leituras.filter(maquina_id=maquina)
        serializer = LeituraTelemetriaSerializer(leituras[:50], many=True)
        return Response(serializer.data)


class UltimaLeituraView(APIView):
    """
    Retorna a leitura mais recente de cada máquina ativa.
    Opcionalmente filtra por maquina_id.

    GET /api/leituras/ultimas/
    GET /api/leituras/ultimas/?maquina_id=COLH-01

    Resposta:
    [
        {
            "maquina_id": "COLH-01",
            "temperatura": 87.3,
            "vibracao": 0.45,
            "rpm": 1850,
            "timestamp": "2026-04-10T14:32:01",
            "nivel_risco": "CRITICO",
            "total_leituras": 124
        }
    ]
    """

    def get(self, request):
        maquina = request.query_params.get('maquina_id')

        # pega IDs únicos de máquinas que têm leituras
        qs = LeituraTelemetria.objects.all()
        if maquina:
            qs = qs.filter(maquina_id=maquina)

        # descobre quais máquinas existem no banco
        maquinas = qs.values_list('maquina_id', flat=True).distinct()

        resultado = []
        for mid in maquinas:
            ultima = (
                LeituraTelemetria.objects
                .filter(maquina_id=mid)
                .order_by('-timestamp')
                .first()
            )
            if not ultima:
                continue

            total = LeituraTelemetria.objects.filter(maquina_id=mid).count()

            # classifica risco por regra simples
            # quando o Random Forest estiver pronto, isso vira uma chamada ao modelo
            if ultima.temperatura > 85 or ultima.vibracao > 0.8:
                nivel = 'CRITICO'
            elif ultima.temperatura > 75 or ultima.vibracao > 0.5:
                nivel = 'ATENCAO'
            else:
                nivel = 'NORMAL'

            resultado.append({
                'maquina_id':     mid,
                'temperatura':    ultima.temperatura,
                'vibracao':       ultima.vibracao,
                'rpm':            ultima.rpm,
                'timestamp':      ultima.timestamp,
                'nivel_risco':    nivel,
                'total_leituras': total,
            })

        return Response(resultado)


class ManutencaoView(APIView):
    """
    GET /api/manutencao/?maquina_id=COLH-01

    Prevê probabilidade de necessidade de manutenção.
    Precisa de pelo menos 30 leituras da máquina especificada.
    """
    def get(self, request):
        maquina = request.query_params.get('maquina_id')
        if not maquina:
            return Response(
                {'status': 'erro', 'detalhe': 'maquina_id é obrigatório'},
                status=400
            )
        resultado = prever_manutencao(maquina_id=maquina)
        return Response(resultado)
