from django.views import generic
from pyrio.eventos.models import Evento


class IndexView(generic.DetailView):
    template_name = 'index.html'
    context_object_name = 'evento'

    def get_object(self, queryset=None):
        return Evento.objects.get_edicao_atual()
