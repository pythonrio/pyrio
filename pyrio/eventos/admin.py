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
        # TODO(andre): Copiar parceiros e talvez palestrantes
        for instance in queryset:
            instance.pk = None
            instance.nome += ' (Cópia)'
            instance.save()

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
