from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioList(ListView):
    model = User
    template_name = "usuario_list.html"

# class = UsuarioCreateView(CreateView):
#     model = User
#     form_class = UserCreationForm
