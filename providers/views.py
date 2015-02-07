from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.providers.tables import PostsTable
from openstack_dashboard.dashboards.integra.providers import utils
from openstack_dashboard.dashboards.integra.providers.workflows.create_post import CreatePost

class PostIndexView(tables.DataTableView):
    table_class = PostsTable
    template_name = 'integra/providers/index.html'

    def get_data(self):
        return utils.get_posts(self)

class PostCreateView(workflows.WorkflowView):
    workflow_class = CreatePost

    def get_initial(self):
        initial = super(PostCreateView, self).get_initial()
        return initial
