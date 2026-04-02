import json
import logging

import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from django.utils import timezone

from api_tcc.models import LeituraTelemetria

logger = logging.getLogger(__name__)

BROKER_HOST = 'localhost'
BROKER_PORT = 1883
TOPIC       = 'fieldnode/#'


class Command(BaseCommand):
    help = 'Escuta o broker MQTT e salva leituras do ESP32 no banco.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(
            f'Conectando ao broker MQTT {BROKER_HOST}:{BROKER_PORT} ...'
        ))

        client = mqtt.Client(client_id='fieldnode-django')
        client.on_connect  = self._on_connect
        client.on_message  = self._on_message
        client.on_disconnect = self._on_disconnect

        client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
        client.loop_forever()

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.stdout.write(self.style.SUCCESS('Conectado. Aguardando mensagens...'))
            client.subscribe(TOPIC)
        else:
            self.stderr.write(f'Falha na conexão — código {rc}')

    def _on_disconnect(self, client, userdata, rc):
        self.stderr.write(f'Desconectado do broker (rc={rc}). Reconectando...')

    def _on_message(self, client, userdata, msg):
        try:
            data = json.loads(msg.payload.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            self.stderr.write(f'Payload inválido em {msg.topic}: {exc}')
            return

        uuid_recebido = data.get('id')
        maquina_id    = str(data.get('maquina_id', '')).strip()

        if not maquina_id:
            self.stderr.write('Mensagem ignorada: maquina_id ausente.')
            return

        defaults = {
            'maquina_id':  maquina_id,
            'temperatura': float(data.get('temperatura', 0)),
            'vibracao':    float(data.get('vibracao', 0)),
            'rpm':         int(data.get('rpm', 0)),
            'timestamp':   parse_datetime(str(data.get('timestamp', ''))) or timezone.now(),
        }

        if uuid_recebido:
            _, created = LeituraTelemetria.objects.get_or_create(
                id=uuid_recebido,
                defaults=defaults,
            )
            status = 'salva' if created else 'duplicata ignorada'
        else:
            LeituraTelemetria.objects.create(**defaults)
            status = 'salva (sem UUID)'

        self.stdout.write(f'[{maquina_id}] {status} — {defaults["temperatura"]}°C  {defaults["rpm"]} RPM')
