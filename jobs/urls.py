from django.conf.urls import patterns, url
from openstack_dashboard.dashboards.integra.jobs import views

INDEX_URL = r'^$'
#CREATE_URL = r'^create'

urlpatterns = patterns('openstack_dashboard.dashboards.integra.jobs.views',
    url(INDEX_URL, views.JobIndexView.as_view(), name='index'),
    #url(CREATE_URL, views.PostCreateView.as_view(), name='create'),
)