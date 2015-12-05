from django.contrib import admin

from pyrio.eventos import models


@admin.register(models.Edicao)
class EdicaoAdmin(admin.ModelAdmin):
    list_display = [
        'local',
        'data',
    ]


@admin.register(models.Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = [
        'hora',
        'descricao',
        'responsavel',
    ]


@admin.register(models.Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    pass
