from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from conta.models import Conta
from lancamento.models import Lancamento

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        saldos_contas = []
        for conta in Conta.objects.ativas():
            saldos_contas.append(['%s - R$ %d'%(conta.descricao, conta.get_saldo), str(conta.get_saldo).replace(',','.')])
        context['saldos_contas'] = saldos_contas

        context['saldo_total'] = Conta.objects.get_somatorio_saldo_contas_ativas()

        context['lancamentos_pendentes'] = Lancamento.objects.pendentes()

        return context
