from django.conf.urls import include, url
from usuario.views import UsuarioList

urlpatterns = [
    url(r'^list$', UsuarioList.as_view(), name='usuario_list'),
]
