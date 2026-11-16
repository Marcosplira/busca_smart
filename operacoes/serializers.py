from rest_framework import serializers
from .models import Operacao, SetorRota, PontoSinalizacao


class OperacaoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Operacao
    fields = [
        'id',
        'nome',
        'descricao',
        'codigo_convite',
        'area_delimitada_geojson',
        'area_total_km2',
        'status',
        'criado_em',
    ]
    read_only_fields = ['codigo_convite', 'criado_em']


class SetorRotaSerializer(serializers.ModelSerializer):

  class Meta:
    model = SetorRota
    fields = [
        'id',
        'operacao',
        'identificacao',
        'cor_hex',
        'poligono_setor_geojson',
        'rota_planejada_geojson',
        'instrucoes_especificas',
        'concluido',
    ]


class PontoSinalizacaoSerializer(serializers.ModelSerializer):

  class Meta:
    model = PontoSinalizacao
    fields = [
        'id',
        'operacao',
        'setor',
        'titulo',
        'tipo',
        'descricao',
        'latitude',
        'longitude',
        'criado_em',
    ]