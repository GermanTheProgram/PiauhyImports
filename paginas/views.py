'''from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request, "home.html")
'''

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
