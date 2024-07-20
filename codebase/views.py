from django.shortcuts import render
from .models import CRUD
from .forms import CRUDFORM
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import reverse


class Home(ListView):
  model = CRUD
  template_name = 'list.html'


class Create(CreateView):
  model = CRUD
  template_name = 'create.html'
  form_class = CRUDFORM  #our form class

  def get_success_url(self):
    return reverse('home')


class Detail(DetailView):
  model = CRUD
  template_name = 'detail.html'


class Update(UpdateView):
  model = CRUD
  template_name = 'create.html'  #same create
  form_class = CRUDFORM  #our form class

  def get_success_url(self):
    return reverse('home')


class Delete(DeleteView):
  model = CRUD
  template_name = 'delete.html'

  def get_success_url(self):
    return reverse('home')  #navigateTo
