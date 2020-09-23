from django.urls import path
from django.conf.urls import url
from .views import index, project, task_delete

urlpatterns = [

    path('', index, name='index'),
    path('project', project, name='project'),
    path('projects/<int:project_id>', project, name='projects'),
    url(r'^delete/(?P<pk>[0-9]+)/$', task_delete, name='task_delete')
]
