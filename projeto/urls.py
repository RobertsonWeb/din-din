from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'projeto.views.home', name='home'),
    url(r'^$', include('core.urls')),
    url(r'^conta/', include('conta.urls')),
    url(r'^lancamento/', include('lancamento.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


urlpatterns += patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name':'core/accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', {'template_name':'core/accounts/password_change.html'}, name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name':'core/accounts/password_change_done.html'}, name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name':'core/accounts/password_reset.html'}, name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name':'core/accounts/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', {'template_name':'core/accounts/reset.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name':'core/accounts/reset_done.html'}, name='password_reset_complete'),
)
