from django.contrib import admin

from pyrio.eventos import models


class ParceiroInline(admin.TabularInline):
    model = models.Parceiro


class PalestraInline(admin.TabularInline):
    model = models.Palestra


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

    actions = [
        'copiar_evento',
    ]

    inlines = [
        PalestraInline,
        ParceiroInline,
    ]

    def copiar_evento(self, request, queryset):
        for instance in queryset:
            instance.pk = None
            instance.nome += ' (Cópia)'
            instance.save()


@admin.register(models.Palestrante)
class PalestranteAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
    ]
