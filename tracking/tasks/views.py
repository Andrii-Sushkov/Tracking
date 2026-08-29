from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'status', 'priority', 'content', 'image']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    permission_required = 'tasks.add-task'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    permission_required = 'tasks.change-task'

class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    permission_required = 'tasks.delete-task'