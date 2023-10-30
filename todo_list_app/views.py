from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo_list/task_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo_list/task_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "todo_list/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo_list/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")


class UndoOrCompleteTaskView(View):
    @staticmethod
    def post(request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(
            reverse_lazy("todo_list:task-list")
        )
