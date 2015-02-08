import traceback

from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.integra.schedules import utils


class AddTaskDetailsAction(workflows.Action):

    scheduleId = forms.IntegerField(
        label=_("ScheduleId)"),
        required=True,
        min_value=1,
        max_value=9999999,
        help_text=_("ScheduleId"))

    name = forms.CharField(
        label=_("Name"),
        required=True,
        max_length=80,
        help_text=_("Name"))

    description = forms.CharField(
        label=_("Description"),
        required=True,
        max_length=120,
        help_text=_("Description"))

    hour = forms.IntegerField(
        label=_("Hour)"),
        required=True,
        min_value=1,
        max_value=12,
        help_text=_("1-12"))

    min = forms.IntegerField(
        label=_("Minute"),
        required=True,
        min_value=0,
        max_value=59,
        help_text=_("0 - 59"))

    period = forms.ChoiceField(
        label=_("Period"),
        choices=[('AM', 'AM'), ('PM', 'PM')],
        required=True,
        help_text=_("AM or PM"))

    start = forms.DateField(
        label=_("Start date"), required=False,
        input_formats=("%Y-%m-%d",),
        help_text=_("YYYY-MM-DD"),
        widget=forms.DateInput(attrs={'data-date-format': 'yyyy-mm-dd'}))

    end = forms.DateField(
        label=_("End date"), required=True,
        input_formats=("%Y-%m-%d",),
        help_text=_("YYYY-MM-DD"),
        widget=forms.DateInput(attrs={'data-date-format': 'yyyy-mm-dd'}))

    enabled = forms.BooleanField(
        label=_("Enabled"),
        required=False,
        help_text=_("Enabled"))

    class Meta:
        name = _("Details")

    def __init__(self, request, context, *args, **kwargs):
        self.request = request
        self.context = context
        super(AddTaskDetailsAction, self).__init__(
            request, context, *args, **kwargs)

class SetAddTaskDetails(workflows.Step):
    action_class = AddTaskDetailsAction
    contributes = ("scheduleId", "name", "description", "hour", "min", "period", "start", "end", "enabled")

    def contribute(self, data, context):
        if data:
            context['scheduleId'] = data.get("scheduleId", "")
            context['name'] = data.get("name", "")
            context['description'] = data.get("description", "")
            context['hour'] = data.get("hour", "")
            context['min'] = data.get("min", "")
            context['period'] = data.get("period", "")
            context['start'] = data.get("start", "")
            context['end'] = data.get("end", "")
            context['enabled'] = data.get("enabled", "")
        return context


# =====
# Create the post
# =====

class AddTask(workflows.Workflow):
    slug = "addTask"
    name = _("Add Task")
    finalize_button_name = _("Add Task")
    success_message = _('Added task "%s".')
    failure_message = _('Unable to add task "%s".')
    success_url = "horizon:integra:schedules:index"
    failure_url = "horizon:integra:schedules:index"
    default_steps = (SetAddTaskDetails,)

    def format_status_message(self, message):
         return message % self.context.get('name', 'unknown task')

    def handle(self, request, context):
        try:
            for k, v in context.items():
                print(k, v)
                print("-----------------")
            print("===================")
            utils.addTaskToSchedule(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to add task"))
            return False
