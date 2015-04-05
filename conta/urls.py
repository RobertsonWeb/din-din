from django.conf.urls import patterns, url
from conta.views import ContaCreate, ContaList, ContaUpdate, ContaDelete

urlpatterns = patterns('',
    url(r'add/$', ContaCreate.as_view(), name='conta_add'),
    url(r'list/$', ContaList.as_view(), name='conta_list'),
    url(r'(?P<pk>\d+)/$', ContaUpdate.as_view(), name='conta_update'),
    url(r'(?P<pk>\d+)/delete$', ContaDelete.as_view(), name='conta_delete'),
)
