from django.conf.urls import patterns, url
from openstack_dashboard.dashboards.integra.add_provider import views

INDEX_URL = r'^$'
CREATE_URL = r'^create'

urlpatterns = patterns('openstack_dashboard.dashboards.integra.add_provider.views',
    url(INDEX_URL, views.PostIndexView.as_view(), name='index'),
)