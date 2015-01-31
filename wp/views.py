import traceback

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.wp.tables import PostsTable
from openstack_dashboard.dashboards.integra.wp.post.post import Post
from openstack_dashboard.dashboards.integra.wp import utils
from openstack_dashboard.dashboards.integra.wp.workflows.create_post import CreatePost

class PostIndexView(tables.DataTableView):
    table_class = PostsTable
    template_name = 'integra/wp/index.html'

    def get_data(self):
        return utils.get_posts(self)

class PostCreateView(workflows.WorkflowView):
    workflow_class = CreatePost

    def get_initial(self):
        initial = super(PostCreateView, self).get_initial()
        return initial
