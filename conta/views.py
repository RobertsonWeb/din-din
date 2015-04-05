from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from conta.models import Conta

class ContaCreate(CreateView):
    model = Conta
    fields = ['descricao', 'ativa']
    success_url = 'conta_list'


class ContaList(ListView):
    model = Conta

class ContaUpdate(UpdateView):
    model = Conta
    fields = ['descricao', 'ativa']
    success_url = 'conta_list'

class ContaDelete(DeleteView):
    model = Conta
    success_url = 'conta_list'
