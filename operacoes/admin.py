from django.contrib import admin
from django.utils.html import format_html
from .models import Operacao, SetorRota, PontoSinalizacao

# Personalização Visual do Painel Django Admin
admin.site.site_header = "⚡ BuscaSmart — Painel de Gestão SAR"
admin.site.site_title = "BuscaSmart Administração"
admin.site.index_title = "Comando Central de Operações e Usuários"


class SetorRotaInline(admin.TabularInline):
    model = SetorRota
    extra = 1
    fields = ('identificacao', 'responsavel', 'cor_hex', 'concluido', 'instrucoes_especificas')
    show_change_link = True


class PontoSinalizacaoInline(admin.TabularInline):
    model = PontoSinalizacao
    extra = 1
    fields = ('tipo', 'titulo', 'latitude', 'longitude', 'criado_por')
    show_change_link = True


@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'badge_codigo', 'status_colorido', 'area_display', 'coordenador', 'criado_em')
    list_filter = ('status', 'criado_em', 'coordenador')
    search_fields = ('nome', 'codigo_convite', 'descricao')
    readonly_fields = ('codigo_convite', 'criado_em', 'atualizado_em')
    inlines = [SetorRotaInline, PontoSinalizacaoInline]
    
    fieldsets = (
        ('Identificação da Missão', {
            'fields': ('nome', 'descricao', 'status', 'coordenador', 'codigo_convite')
        }),
        ('Informações Geográficas', {
            'fields': ('area_total_km2', 'versao', 'area_delimitada_geojson')
        }),
        ('Datas de Registro', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )

    def badge_codigo(self, obj):
        return format_html(
            '<span style="background: #0f172a; color: #38bdf8; padding: 3px 8px; border-radius: 6px; font-family: monospace; font-weight: bold; border: 1px solid #1e293b;">{}</span>',
            obj.codigo_convite
        )
    badge_codigo.short_description = "Código de Acesso"

    def status_colorido(self, obj):
        cores = {
            'ANDAMENTO': '#10b981',
            'PLANEJAMENTO': '#f59e0b',
            'CONCLUIDA': '#3b82f6'
        }
        cor = cores.get(obj.status, '#94a3b8')
        return format_html(
            '<span style="color: {}; font-weight: bold; border: 1px solid {}; padding: 2px 8px; border-radius: 12px;">● {}</span>',
            cor, cor, obj.get_status_display()
        )
    status_colorido.short_description = "Status Operacional"

    def area_display(self, obj):
        return f"{obj.area_total_km2} km² ({round(obj.area_total_km2 * 100, 1)} ha)"
    area_display.short_description = "Área Total"


@admin.register(SetorRota)
class SetorRotaAdmin(admin.ModelAdmin):
    list_display = ('identificacao', 'tag_cor', 'operacao', 'responsavel', 'status_conclusao', 'atualizado_em')
    list_filter = ('concluido', 'operacao', 'responsavel')
    search_fields = ('identificacao', 'instrucoes_especificas', 'operacao__nome')

    def tag_cor(self, obj):
        return format_html(
            '<span style="display: inline-block; width: 14px; height: 14px; background-color: {}; border-radius: 50%; vertical-align: middle; margin-right: 6px; border: 1px solid rgba(0,0,0,0.2);"></span><span>{}</span>',
            obj.cor_hex, obj.cor_hex
        )
    tag_cor.short_description = "Cor do Setor"

    def status_conclusao(self, obj):
        if obj.concluido:
            return format_html('<span style="color: #10b981; font-weight: bold;">{}</span>', '✓ Varrido / Concluído')
        return format_html('<span style="color: #f59e0b; font-weight: bold;">{}</span>', '⏳ Em Aberto')
    status_conclusao.short_description = "Situação"


@admin.register(PontoSinalizacao)
class PontoSinalizacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_badge', 'operacao', 'coordenadas', 'criado_por', 'criado_em')
    list_filter = ('tipo', 'operacao', 'criado_em')
    search_fields = ('titulo', 'descricao', 'operacao__nome')

    def tipo_badge(self, obj):
        cores = {
            'BASE': '#10b981',
            'ULTIMO_PONTO': '#ef4444',
            'EVIDENCIA': '#f59e0b',
            'OBSTACULO': '#8b5cf6',
            'REFERENCIA': '#06b6d4'
        }
        cor = cores.get(obj.tipo, '#64748b')
        return format_html(
            '<span style="background: {}; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">{}</span>',
            cor, obj.get_tipo_display()
        )
    tipo_badge.short_description = "Tipo de Ponto"

    def coordenadas(self, obj):
        return format_html(
            '<span style="font-family: monospace; color: #0284c7;">{}, {}</span>',
            round(obj.latitude, 5), round(obj.longitude, 5)
        )
    coordenadas.short_description = "GPS (Lat / Lng)"
