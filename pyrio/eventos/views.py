from django.views import generic
from pyrio.eventos.models import Edicao


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        edicao = Edicao().get_edicao_atual()

        return {
            'edicao': edicao,
            'partners': edicao.parceiro_set.all()
        }
