from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.schedules.tables import ScheduleTable
from openstack_dashboard.dashboards.integra.schedules import utils
from openstack_dashboard.dashboards.integra.schedules.workflows.add_schedule import AddSchedule

class PostIndexView(tables.DataTableView):
    table_class = ScheduleTable
    template_name = 'integra/schedules/index.html'

    def get_data(self):
        return utils.getSchedules(self)

class PostCreateView(workflows.WorkflowView):
    workflow_class = AddSchedule

    def get_initial(self):
        initial = super(PostCreateView, self).get_initial()
        return initial
