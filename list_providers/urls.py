from django.conf.urls import patterns, url
from openstack_dashboard.dashboards.integra.list_providers import views

INDEX_URL = r'^$'
CREATE_URL = r'^create'

urlpatterns = patterns('openstack_dashboard.dashboards.integra.list_providers.views',
    url(INDEX_URL, views.ProvidersView.as_view(), name='index'),
)