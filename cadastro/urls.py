from django.urls import path
from .views import form_modelform


urlpatterns = [
    path('login/', form_modelform, name='login')
]