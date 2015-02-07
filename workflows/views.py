from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.workflows.tables import WorkflowTable
from openstack_dashboard.dashboards.integra.workflows import utils
from openstack_dashboard.dashboards.integra.workflows.workflows.add_workflow import AddWorkflow

class PostIndexView(tables.DataTableView):
    table_class = WorkflowTable
    template_name = 'integra/workflows/index.html'

    def get_data(self):
        return utils.getWorkflows(self)

class PostCreateView(workflows.WorkflowView):
    workflow_class = AddWorkflow

    def get_initial(self):
        initial = super(PostCreateView, self).get_initial()
        return initial
