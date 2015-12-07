from django.contrib import admin
from django.utils import timezone

from pyrio.eventos import models


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
                ('nome', 'slug'),
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
        ('Parceiros', {
            'fields': (
                'parceiros',
            )
        }),
    ]

    readonly_fields = [
        'slug',
    ]

    filter_horizontal = [
        'parceiros',
    ]

    actions = [
        'copiar_evento',
    ]

    inlines = [
        PalestraInline,
    ]

    def copiar_evento(self, request, queryset):
        for instance in queryset:
            parceiros = [p.pk for p in instance.parceiros.all()]

            instance.pk = None
            instance.nome += ' (Cópia)'.format(timezone.now())
            instance.save()

            instance.parceiros.add(*parceiros)

        if len(queryset) > 1:
            message = 'eventos foram copiados com sucesso.'
        else:
            message = 'evento foi copiado com sucesso.'

        self.message_user(request, '{} {}'.format(len(queryset), message))

    copiar_evento.short_description = 'Copiar Eventos selecionados'


@admin.register(models.Palestrante)
class PalestranteAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
    ]


@admin.register(models.Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
    ]
