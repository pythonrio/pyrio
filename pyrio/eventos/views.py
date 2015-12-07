from django.views import generic
from pyrio.eventos.models import Evento


class IndexView(generic.DetailView):
    template_name = 'index.html'
    context_object_name = 'evento'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if pk:
            return Evento.objects.get(pk=pk, slug=slug)

        return Evento.objects.get_edicao_atual()
