import traceback

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.schedules.tables import PostsTable
from openstack_dashboard.dashboards.integra.schedules.post.post import Post
from openstack_dashboard.dashboards.integra.schedules import utils
from openstack_dashboard.dashboards.integra.schedules.workflows.create_post import CreatePost

class PostIndexView(tables.DataTableView):
    table_class = PostsTable
    template_name = 'integra/schedules/index.html'

    def get_data(self):
        return utils.get_posts(self)

class PostCreateView(workflows.WorkflowView):
    workflow_class = CreatePost

    def get_initial(self):
        initial = super(PostCreateView, self).get_initial()
        return initial
