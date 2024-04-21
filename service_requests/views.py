from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from .models import Request
from .forms import RequestForm

class RequestCreate(CreateView):
    model = Request
    form = RequestForm
    template_name = 'request_form.html'
    fields = ['req_type','details']
    success_url = '/request-submitted/'

class RequestList(ListView):
    model = Request
    template_name = 'request_list.html'
    context_object_name = 'requests'

class Requestupdate(UpdateView):
    model = Request
    fields = ['status']
    template_name = 'request_update.html'
    success_url = '/request-updated/'

# Create your views here.
