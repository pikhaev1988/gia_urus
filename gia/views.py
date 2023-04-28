from django.shortcuts import render
from django.views.generic import CreateView
from gia.form import *
from django.urls import reverse_lazy

def index(req):
    return render(req, 'gia/index.html')

class regist(CreateView):
    form_class = register
    template_name = 'gia/register.html'
    success_url = reverse_lazy('index')
