from django.conf.urls import include, url
from core.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
