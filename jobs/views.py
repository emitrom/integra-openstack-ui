from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.jobs.tables import JobsTable
from openstack_dashboard.dashboards.integra.jobs import utils

class JobIndexView(tables.DataTableView):
    table_class = JobsTable
    template_name = 'integra/jobs/index.html'

    def get_data(self):
        return utils.getJobs(self)

#class JobCreateView(workflows.WorkflowView):
#    workflow_class = AddProvider#

#    def get_initial(self):
#        initial = super(JobCreateView, self).get_initial()
#        return initial
