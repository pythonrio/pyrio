from django.contrib import admin

from pyrio.eventos import models


@admin.register(models.Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'local',
        'data',
    ]

    fieldsets = [
        ('Dados do Evento', {
            'fields': (
                'nome',
                'data',
                'sobre',
                'inscricoes',
            )
        }),
        ('Localização', {
            'fields': (
                ('local', 'cidade'),
                'endereco',
            )
        }),
    ]


@admin.register(models.Palestrante)
class PalestranteAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
    ]


@admin.register(models.Palestra)
class PalestraAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
    ]

    list_filter = [
        'evento',
    ]


@admin.register(models.Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
    ]

    list_filter = [
        'evento',
    ]
