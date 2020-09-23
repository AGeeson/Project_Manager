from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import Project, Task
from .forms import TaskForm, EditForm, ProjectForm


def index(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    for project in projects:
        project.task_count = tasks.filter(project__id=project.id).count()
        project.essential_task_count = tasks.filter(
            project__id=project.id, essential=True).count()
        if project.essential_task_count == 0:
            project.essential_percent_complete = 100
        else:
            project.essential_percent_complete = ((tasks.filter(
                project__id=project.id, progress='COMPLETED').count()) / (tasks.filter(
                    project__id=project.id, essential=True).count())) * 100

    if request.method != 'POST':
        form = ProjectForm()
    else:
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
    context = {
        'projects': projects,
        'tasks': tasks,
        'form': form}
    return render(request, 'index.html', context)


def project(request, project_id):
    projects = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project_id=project_id)
    todo = []
    inprogress = []
    toverify = []
    bugged = []
    completed = []
    for task in tasks:
        project = task.project
        if task.progress == 'To Do':
            todo.append(task)
        elif task.progress == 'In Progress':
            inprogress.append(task)
        elif task.progress == 'To Verify':
            toverify.append(task)
        elif task.progress == 'Bugged':
            bugged.append(task)
        elif task.progress == 'Completed':
            completed.append(task)
        else:
            pass

    if request.method != 'POST':
        form = TaskForm()

    elif request.method == 'POST':
        form = TaskForm(data=request.POST)

        if request.POST.get("save"):
            for task in tasks:
                # chaneg progress status and creates timestamp/log when done
                progress = ["To Do", "In Progress",
                            "To Verfiy", "Buggged", "Completed"]
                for item in progress:
                    if request.POST.get("c" + str(task.id)) == item:
                        if task.progress != item:
                            log = task.logs.create(task_progress=item,
                                                   task_progress_prior=task.progress)
                            task.progress = item
                            """task.progress = item
                            log.task_progress = task.progress"""
                if request.POST.get("e" + str(task.id)) == "clicked":
                    task.essential = True
                else:
                    task.essential = False
                task.save()

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.project_id = projects.id
            new_entry.save()
        return HttpResponseRedirect(reverse('projects', args=[project_id]))
    context = {'projects': projects,
               'tasks': tasks,
               'todo': todo,
               'inprogress': inprogress,
               'toverify': toverify,
               'bugged': bugged,
               'completed': completed,
               'form': form}
    return render(request, 'project.html', context)


# edit_entry(request, task_id)
"""	if request.method != 'POST':
		form = CommentForm()
	else:
		form = CommentForm(data=request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.location = location
			new_comment.owner = request.user

			new_comment.save()
			return HttpResponseRedirect(reverse('location', args=[location_id]))"""


# Create your views here.
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project_id = task.project.id
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect(reverse('projects', args=[project_id]))

    return render(request, 'project.html', {'task': task})
