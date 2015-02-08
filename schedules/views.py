from horizon import exceptions, tables, workflows, forms, tabs

from openstack_dashboard.dashboards.integra.schedules.tables import ScheduleTable
from openstack_dashboard.dashboards.integra.schedules import utils
from openstack_dashboard.dashboards.integra.schedules.workflows.add_schedule import AddSchedule
from openstack_dashboard.dashboards.integra.schedules.workflows.add_task import AddTask

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

class AddTaskView(workflows.WorkflowView):
    workflow_class = AddTask

    def get_context_data(self, **kwargs):
        context = super(AddTaskView, self).get_context_data(**kwargs)
        # Data from URL are always in self.kwargs, here we pass the data
        # to the template.
        #context["source_id"] = self.kwargs['source_id']
        # Data contributed by Workflow's Steps are in the
        # context['workflow'].context list. We can use that in the
        # template too.
        return context

    def get_initial(self):
        initial = super(AddTaskView, self).get_initial()
        return initial
