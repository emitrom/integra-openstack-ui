from django.conf.urls import patterns, url
from openstack_dashboard.dashboards.integra.schedules import views

INDEX_URL = r'^$'
CREATE_URL = r'^create'
ADD_TASK_URL = r'^addTask'

urlpatterns = patterns('openstack_dashboard.dashboards.integra.schedules.views',
    url(INDEX_URL, views.PostIndexView.as_view(), name='index'),
    url(CREATE_URL, views.PostCreateView.as_view(), name='create'),
    url(ADD_TASK_URL, views.AddTaskView.as_view(), name='addTask'),
)