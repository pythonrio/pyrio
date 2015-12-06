from django.utils import timezone
from django.db import models


class EventoQuerySet(models.QuerySet):
    def get_edicao_atual(self):
        edicao_atual = self.filter(data__gte=timezone.now()).first()

        if not edicao_atual:
            self.latest('data')

        return edicao_atual


class Evento(models.Model):
    nome = models.CharField(
        verbose_name='Nome do Evento',
        max_length=90,
        help_text='Ex.: Meetup PythonRio',
    )

    data = models.DateTimeField(
        verbose_name='Inicio do Evento',
    )

    local = models.CharField(
        verbose_name='Local do Evento',
        max_length=90,
        help_text='Nome da empresa, faculdade, etc... aonde irá acontecer o evento. Ex.: Hotel Urbano.'
    )

    cidade = models.CharField(
        verbose_name='Cidade',
        max_length=90,
    )

    # estado

    endereco = models.CharField(
        verbose_name='Endereço do Evento',
        max_length=90,
        help_text='Endereço completo do local do evento.'
    )

    sobre = models.TextField(
        verbose_name='Descrição do evento',
        help_text='Sobre o evento, o que vai acontecer, publico alvo, etc...',
    )

    inscricoes = models.URLField(
        verbose_name='URL para as incrições',
    )

    objects = EventoQuerySet.as_manager()

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return '{}'.format(self.nome)


class Palestrante(models.Model):
    nome = models.CharField(max_length=90)
    foto = models.ImageField(upload_to='palestrantes/', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    sobre = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return '{}'.format(self.nome)


class Palestra(models.Model):
    evento = models.ForeignKey(
        to='Evento',
        related_name='palestras',
    )

    titulo = models.CharField(max_length=90)

    palestrante = models.ForeignKey(
        to='Palestrante',
        related_name='palestras',
    )

    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'

    def __str__(self):
        return '{}'.format(self.titulo)


class Parceiro(models.Model):
    evento = models.ForeignKey(
        to='Evento',
        related_name='parceiros',
    )

    nome = models.CharField(max_length=90)
    logo = models.ImageField(upload_to='parceiros/')
    # site

    class Meta:
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'

    def __str__(self):
        return '{}'.format(self.nome)
