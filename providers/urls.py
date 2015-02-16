from django.conf.urls import patterns, url
from openstack_dashboard.dashboards.integra.providers import views

INDEX_URL = r'^$'
ADD_PROVIDER_URL = r'^add'

urlpatterns = patterns('openstack_dashboard.dashboards.integra.providers.views',
    url(INDEX_URL, views.ProvidersIndexView.as_view(), name='index'),
    url(ADD_PROVIDER_URL, views.AddProviderView.as_view(), name='add'),
)