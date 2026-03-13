from rest_framework import serializers
from rest_framework import viewsets
from api_tcc import models
from api_tcc.api import serializers
from drf_yasg.utils import swagger_auto_schema

class UnidadedeMedidaViewSet(viewsets.ModelViewSet):
    queryset = models.UnidadedeMedida.objects.all()
    serializer_class = serializers.UnidadedeMedidaSerializer
    
    # decoradores para documentação do swagger, descrevendo cada endpoint e os tipos de resposta esperados  
    
    @swagger_auto_schema( 
        operation_description="Retorna todas os tipos de unidade de medida",
        responses={200: serializers.UnidadedeMedidaSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        
        return super().list(request, *args, **kwargs)
    # Retorna todas os tipos de unidade de medida, utilizando o serializer para formatar a resposta, e o decorador para documentar a operação no swagger
    # Método GET, endpoint /unidadedemedida/ (listagem de unidades de medida)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de unidade de medida",
        responses={201: serializers.UnidadedeMedidaSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    # Cria um novo registro de unidade de medida, utilizando o serializer para validar e salvar os dados, e o decorador para documentar a operação no swagger
    # Método POST, endpoint /unidadedemedida/ (criação de unidade de medida)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de unidade de medida conforme o ID fornecido",
        responses={200: serializers.UnidadedeMedidaSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    # Retorna o registro de unidade de medida conforme o ID fornecido, utilizando o serializer para formatar a resposta, e o decorador para documentar a operação no swagger
    # Método GET ID, endpoint /unidadedemedida/{id}/ (detalhes de uma unidade de medida específica)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de unidade de medida conforme o dados passados para o ID fornecido",
        responses={200: serializers.UnidadedeMedidaSerializer(many=True)},
    )
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    # Altera o registro de unidade de medida conforme os dados passados para o ID fornecido, utilizando o serializer para validar e salvar os dados, e o decorador para documentar a operação no swagger
    # Método PUT ID, endpoint /unidadedemedida/{id}/ (atualização de uma unidade de medida específica)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de unidade de medida conforme o ID fornecido",
        responses={204: serializers.UnidadedeMedidaSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    # Deleta o registro de unidade de medida conforme o ID fornecido, utilizando o decorador para documentar a operação no swagger
    # Método DELETE ID, endpoint /unidadedemedida/{id}/ (remoção de uma unidade de medida específica)
 
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas as marcas",
        responses={200: serializers.MarcaSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    # Retorna todas as marcas, utilizando o serializer para formatar a resposta, e o decorador para documentar a operação no swagger
    # Método GET, endpoint /marca/ (listagem de marcas)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de marca",
        responses={201: serializers.MarcaSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    # Cria um novo registro de marca, utilizando o serializer para validar e salvar os dados, e o decorador para documentar a operação no swagger
    # Método POST, endpoint /marca/ (criação de marca)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de marca conforme o ID fornecido",
        responses={200: serializers.MarcaSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    # Retorna o registro de marca conforme o ID fornecido, utilizando o serializer para formatar a resposta, e o decorador para documentar a operação no swagger
    # Método GET ID, endpoint /marca/{id}/ (detalhes de uma marca
    
    @swagger_auto_schema(
        operation_description="Altera o registro de marca conforme o dados passados para o ID fornecido",
        responses={200: serializers.MarcaSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    # Altera o registro de marca conforme os dados passados para o ID fornecido, utilizando o serializer para validar e salvar os dados, e o decorador para documentar a operação no swagger
    # Método PUT ID, endpoint /marca/{id}/ (atualização de uma marca específica)

    @swagger_auto_schema(
        operation_description="Deleta o registro de marca conforme o ID fornecido",
        responses={204: serializers.MarcaSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = models.Modelo.objects.all()
    serializer_class = serializers.ModeloSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todos os modelos",
        responses={200: serializers.ModeloSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de modelo",
        responses={201: serializers.ModeloSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de modelo conforme o ID fornecido",
        responses={200: serializers.ModeloSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de modelo conforme o dados passados para o ID fornecido",
        responses={200: serializers.ModeloSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de modelo conforme o ID fornecido",
        responses={204: serializers.ModeloSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CombustivelViewSet(viewsets.ModelViewSet):
    queryset = models.Combustivel.objects.all()
    serializer_class = serializers.CombustivelSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todos os tipos de combustível",
        responses={200: serializers.CombustivelSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de tipo de combustível",
        responses={201: serializers.CombustivelSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de tipo de combustível conforme o ID fornecido",
        responses={200: serializers.CombustivelSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de tipo de combustível conforme o dados passados para o ID fornecido",
        responses={200: serializers.CombustivelSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de tipo de combustível conforme o ID fornecido",   
        responses={204: serializers.CombustivelSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class OperarioViewSet(viewsets.ModelViewSet):
    queryset = models.Operario.objects.all()
    serializer_class = serializers.OperarioSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todos os operários",
        responses={200: serializers.OperarioSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de operário",
        responses={201: serializers.OperarioSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de operário conforme o ID fornecido",
        responses={200: serializers.OperarioSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de operário conforme o dados passados para o ID fornecido",
        responses={200: serializers.OperarioSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de operário conforme o ID fornecido",
        responses={204: serializers.OperarioSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class PressaoPneusViewSet(viewsets.ModelViewSet):
    queryset = models.PressaoPneus.objects.all()
    serializer_class = serializers.PressaoPneusSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas as pressões dos pneus",
        responses={200: serializers.PressaoPneusSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de pressão dos pneus",
        responses={201: serializers.PressaoPneusSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de pressão dos pneus conforme o ID fornecido",
        responses={200: serializers.PressaoPneusSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de pressão dos pneus conforme o dados passados para o ID fornecido",
        responses={200: serializers.PressaoPneusSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de pressão dos pneus conforme o ID fornecido",
        responses={204: serializers.PressaoPneusSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AlturadoCorteViewSet(viewsets.ModelViewSet):
    queryset = models.AlturadoCorte.objects.all()
    serializer_class = serializers.AlturadoCorteSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas as alturas de corte",
        responses={200: serializers.AlturadoCorteSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um novo registro de altura de corte",
        responses={201: serializers.AlturadoCorteSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de altura de corte conforme o ID fornecido",
        responses={200: serializers.AlturadoCorteSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de altura de corte conforme o dados passados para o ID fornecido",
        responses={200: serializers.AlturadoCorteSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de altura de corte conforme o ID fornecido",
        responses={204: serializers.AlturadoCorteSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class PressaodoCorteViewSet(viewsets.ModelViewSet):
    queryset = models.PressaodoCorte.objects.all()
    serializer_class = serializers.PressaodoCorteSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas as pressões de corte",
        responses={200: serializers.PressaodoCorteSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de pressão de corte",
        responses={201: serializers.PressaodoCorteSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de pressão de corte conforme o ID fornecido",
        responses={200: serializers.PressaodoCorteSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de pressão de corte conforme o dados passados para o ID fornecido",
        responses={200: serializers.PressaodoCorteSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de pressão de corte conforme o ID fornecido",
        responses={204: serializers.PressaodoCorteSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):    
        return super().destroy(request, *args, **kwargs)

class TempUmi_AmbienteViewSet(viewsets.ModelViewSet):
    queryset = models.TempUmi_Ambiente.objects.all()
    serializer_class = serializers.TempUmi_AmbienteSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas as temperaturas e umidades do ambiente",
        responses={200: serializers.TempUmi_AmbienteSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de temperatura e umidade do ambiente",
        responses={201: serializers.TempUmi_AmbienteSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de temperatura e umidade do ambiente conforme o  ID fornecido",
        responses={200: serializers.TempUmi_AmbienteSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de temperatura e umidade do ambiente conforme o dados passados para o ID fornecido",
        responses={200: serializers.TempUmi_AmbienteSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de temperatura e umidade do ambiente conforme o ID fornecido",
        responses={204: serializers.TempUmi_AmbienteSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TemperaturaMaquinaViewSet(viewsets.ModelViewSet):
    queryset = models.TemperaturaMaquina.objects.all()
    serializer_class = serializers.TemperaturaMaquinaSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas as temperaturas das máquinas",
        responses={200: serializers.TemperaturaMaquinaSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um novo registro de temperatura da máquina",
        responses={201: serializers.TemperaturaMaquinaSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de temperatura da máquina conforme o ID fornecido",
        responses={200: serializers.TemperaturaMaquinaSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de temperatura da máquina conforme o dados passados para o ID fornecido",
        responses={200: serializers.TemperaturaMaquinaSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de temperatura da máquina conforme o ID fornecido",
        responses={204: serializers.TemperaturaMaquinaSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class StatusdeOperacaoViewSet(viewsets.ModelViewSet):
    queryset = models.StatusdeOperacao.objects.all()
    serializer_class = serializers.StatusdeOperacaoSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas os status de operação",
        responses={200: serializers.StatusdeOperacaoSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de status de operação",
        responses={201: serializers.StatusdeOperacaoSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o resgistro de status de operação conforme o ID fornecido",
        responses={200: serializers.StatusdeOperacaoSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de status de operação conforme o dados passados para o ID fornecido",
        responses={200: serializers.StatusdeOperacaoSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Deleta o registro de status de operação conforme o ID fornecido",
        responses={204: serializers.StatusdeOperacaoSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class EstadodeMovimentoViewSet(viewsets.ModelViewSet):
    queryset = models.EstadodeMovimento.objects.all()
    serializer_class = serializers.EstadodeMovimentoSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas os estados de movimento",
        responses={200: serializers.EstadodeMovimentoSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de estado de movimento",
        responses={201: serializers.EstadodeMovimentoSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de estado de movimento conforme o ID fornecido",
        responses={200: serializers.EstadodeMovimentoSerializer(many=False)},   
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de estado de movimento conforme o dados passados para o ID fornecido",
        responses={200: serializers.EstadodeMovimentoSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de estado de movimento conforme o ID fornecido",
        responses={204: serializers.EstadodeMovimentoSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class TransbordoViewSet(viewsets.ModelViewSet):
    queryset = models.Transbordo.objects.all()
    serializer_class = serializers.TransbordoSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas os transbordos",
        responses={200: serializers.TransbordoSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de transbordo",
        responses={201: serializers.TransbordoSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o resgistro de transbordo conforme o ID fornecido",
        responses={200: serializers.TransbordoSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
class ColheitadeiraViewSet(viewsets.ModelViewSet):
    queryset = models.Colheitadeira.objects.all()
    serializer_class = serializers.ColheitadeiraSerializer
    
    @swagger_auto_schema(
        operation_description="Retorna todas as colheitadeiras",
        responses={200: serializers.ColheitadeiraSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo registro de colheitadeira",
        responses={201: serializers.ColheitadeiraSerializer(many=True)},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o resgistro de colheitadeira conforme o ID fornecido",
        responses={200: serializers.ColheitadeiraSerializer(many=False)},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o registro de colheitadeira conforme o dados passados para o ID fornecido",
        responses={200: serializers.ColheitadeiraSerializer(many=True)},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o registro de colheitadeira conforme o ID fornecido",
        responses={204: serializers.ColheitadeiraSerializer(many=True)},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    