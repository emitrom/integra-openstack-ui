from django.conf.urls import patterns, url
from openstack_dashboard.dashboards.integra.actions import views

INDEX_URL = r'^$'
CREATE_URL = r'^create'

urlpatterns = patterns('openstack_dashboard.dashboards.integra.actions.views',
    url(INDEX_URL, views.PostIndexView.as_view(), name='index'),
    url(CREATE_URL, views.PostCreateView.as_view(), name='create'),
    #url(r'^(?P<image_id>[^/]+)/update/$',
    #    views.UpdateView.as_view(), name='update'),

)