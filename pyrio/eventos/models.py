from django.utils import timezone
from django.db import models


class Edicao(models.Model):
    data = models.DateTimeField()
    local = models.CharField(max_length=255)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    sobre = models.TextField()

    @classmethod
    def get_edicao_atual(cls):
        proxima_edicao = cls.objects.filter(data__gte=timezone.now()).first()
        if not proxima_edicao:
            return cls.objects.latest('data')

        return proxima_edicao

    def __str__(self):
        return '{}'.format(self.data)


class Programa(models.Model):
    edicao = models.ForeignKey('Edicao')

    hora = models.TimeField()
    descricao = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descricao)


class Parceiro(models.Model):
    evento = models.ForeignKey('Edicao')

    nome = models.CharField(max_length=90)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return '{}'.format(self.nome)
