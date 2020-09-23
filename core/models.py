from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    task_count = models.IntegerField(default=0)
    essential_percent_complete = models.DecimalField(
        default=0, decimal_places=20, max_digits=20)
    essential_task_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name.title()[:50]


class Task(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    essential = models.BooleanField(default=False)
    TODO = 'To Do'
    INPROGRESS = 'In Progress'
    TOVERIFY = 'To Verify'
    BUGGGED = 'Bugged'
    COMPLETED = 'Completed'
    PROGRESS = [(TODO, 'To Do'),
                (INPROGRESS, 'In Progress'),
                (TOVERIFY, 'To Verify'),
                (BUGGGED, 'Bugged'),
                (COMPLETED, 'Completed'),
                ]
    progress = models.CharField(
        max_length=30,
        choices=PROGRESS,
        default=TODO,
    )

    def __str__(self):
        return self.name.title()[:50]


class Log(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='logs')
    date_time = models.DateTimeField(auto_now=True, editable=True)
    task_progress = models.CharField(max_length=200)
    task_progress_prior = models.CharField(
        max_length=200, default='To Do')
