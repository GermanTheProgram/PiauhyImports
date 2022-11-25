from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from cadastro.models import Usuario
from .forms import UsuarioForm
from django.urls import reverse_lazy

'''
class UsuarioCad(CreateView):
    template_name = "login.html"
    model = Usuario
    fields = ['nome','email', 'senha']
    success_url = reverse_lazy('login')

    def form_valid(self,form):

        url = super().forms_valid(form)

        return url
'''


def form_modelform(request):

    if request.method == "GET":

        form = UsuarioForm
        context = {
            'form' : form
        }
        return render (request, "login.html", context = context)

    else:
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
        

        context = {
            'form' : form
        }
        return render (request, "login.html", context = context)
