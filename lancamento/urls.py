from django.conf.urls import patterns, url
from lancamento.views import LancamentoCreate, LancamentoList, LancamentoUpdate, LancamentoDelete

urlpatterns = patterns('',
    url(r'add/$', LancamentoCreate.as_view(), name='lancamento_add'),
    url(r'list/$', LancamentoList.as_view(), name='lancamento_list'),
    url(r'(?P<pk>\d+)/$', LancamentoUpdate.as_view(), name='lancamento_update'),
    url(r'(?P<pk>\d+)/delete$', LancamentoDelete.as_view(), name='lancamento_delete'),
)
