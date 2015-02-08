from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.actions.tables import ActionTable
from openstack_dashboard.dashboards.integra.actions import utils
from openstack_dashboard.dashboards.integra.actions.workflows.add_action import AddAction

class PostIndexView(tables.DataTableView):
    table_class = ActionTable
    template_name = 'integra/schedules/index.html'

    def get_data(self):
        return utils.getActions(self)

class PostCreateView(workflows.WorkflowView):
    workflow_class = AddAction

    def get_initial(self):
        initial = super(PostCreateView, self).get_initial()
        return initial
