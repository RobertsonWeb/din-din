from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from lancamento.models import Lancamento

class LancamentoCreate(CreateView):
    model = Lancamento
    fields = ['conta', 'descricao', 'valor',  'data_lancamento', 'situacao', 'classificacao', 'observacao']
    success_url = 'lancamento_list'


class LancamentoList(ListView):
    model = Lancamento

class LancamentoUpdate(UpdateView):
    model = Lancamento
    fields = ['conta', 'descricao', 'valor',  'data_lancamento', 'situacao', 'classificacao', 'observacao']
    success_url = 'lancamento_list'

class LancamentoDelete(DeleteView):
    model = Lancamento
    success_url = 'lancamento_list'
