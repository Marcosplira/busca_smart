import uuid
from django.contrib.auth.models import User
from django.db import models


def gerar_codigo_operacao():
  """Gera um código curto e único para compartilhamento (ex: BUSCA-A1B2C3)"""
  return f'BUSCA-{uuid.uuid4().hex[:6].upper()}'


class Operacao(models.Model):
  STATUS_CHOICES = [
      ('PLANEJAMENTO', 'Em Planejamento'),
      ('ANDAMENTO', 'Em Andamento'),
      ('CONCLUIDA', 'Concluída'),
  ]

  nome = models.CharField(
      max_length=150, verbose_name='Nome da Operação'
  )
  descricao = models.TextField(blank=True, verbose_name='Instruções Gerais')
  codigo_convite = models.CharField(
      max_length=15,
      default=gerar_codigo_operacao,
      unique=True,
      verbose_name='Código de Acesso',
  )
  coordenador = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='operacoes_criadas'
  )

  # Armazena o polígono principal desenhado no mapa em formato GeoJSON
  area_delimitada_geojson = models.JSONField(
      null=True, blank=True, verbose_name='Área Delimitada (GeoJSON)'
  )
  area_total_km2 = models.FloatField(
      default=0.0, verbose_name='Área Total (km²)'
  )

  status = models.CharField(
      max_length=20, choices=STATUS_CHOICES, default='PLANEJAMENTO'
  )
  versao = models.IntegerField(
      default=1, help_text='Incrementado a cada atualização de rota'
  )
  criado_em = models.DateTimeField(auto_now_add=True)
  atualizado_em = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.nome} ({self.codigo_convite})'


class SetorRota(models.Model):
  operacao = models.ForeignKey(
      Operacao, on_delete=models.CASCADE, related_name='setores'
  )
  identificacao = models.CharField(
      max_length=100, help_text='Ex: Rota 01 — Júnior'
  )
  responsavel = models.ForeignKey(
      User,
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      related_name='rotas_atribuidas',
  )
  cor_hex = models.CharField(
      max_length=7,
      default='#3B82F6',
      help_text='Cor visual no mapa (ex: #3B82F6)',
  )

  # Geometrias em GeoJSON para o setor (polígono) e o trajeto (linha)
  poligono_setor_geojson = models.JSONField(null=True, blank=True)
  rota_planejada_geojson = models.JSONField(null=True, blank=True)

  instrucoes_especificas = models.TextField(blank=True)
  concluido = models.BooleanField(default=False)
  atualizado_em = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.identificacao} - {self.operacao.nome}'


class PontoSinalizacao(models.Model):
  TIPO_CHOICES = [
      ('BASE', 'Base de Comando / ICP'),
      ('ULTIMO_PONTO', 'Último Ponto Visto (LKP)'),
      ('EVIDENCIA', 'Possível Evidência / Vestígio'),
      ('OBSTACULO', 'Obstáculo / Área de Risco'),
      ('REFERENCIA', 'Ponto de Referência'),
  ]

  operacao = models.ForeignKey(
      Operacao, on_delete=models.CASCADE, related_name='pontos'
  )
  setor = models.ForeignKey(
      SetorRota, on_delete=models.SET_NULL, null=True, blank=True
  )
  criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  titulo = models.CharField(max_length=100)
  tipo = models.CharField(
      max_length=20, choices=TIPO_CHOICES, default='REFERENCIA'
  )
  descricao = models.TextField(blank=True)
  latitude = models.FloatField()
  longitude = models.FloatField()
  criado_em = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'[{self.get_tipo_display()}] {self.titulo}'