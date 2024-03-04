from asyncio import tasks
from multiprocessing import context
from re import template
from turtle import title
from django.db.models import fields
from django.forms.models import model_to_dict
from django.http import request
from django.shortcuts import redirect, render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView,UpdateView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        print('hello1')
        return reverse_lazy('tasks')
    


class RegisterPage(FormView):
    template_name= 'tasks/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage,self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
  
    model = Task
    context_object_name='tasks'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count

        category_filter = self.request.GET.get('category') or 'all'

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith = search_input)

        if category_filter != 'all':
            context['tasks'] = context['tasks'].filter(category=category_filter)
        
        context['category_filter'] = category_filter
             
        context['search_input']=search_input

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name='task'
    template_name = 'tasks/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description','category','assignee','scheduled_date','estimation_hours','complete']
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model=Task
    fields = ['title','description','category','assignee','scheduled_date','estimation_hours','complete',]
    success_url = reverse_lazy("tasks")

class TaskDelete(LoginRequiredMixin, DeleteView):
    model=Task
    context_object_name='task'
    success_url = reverse_lazy("tasks")
    

