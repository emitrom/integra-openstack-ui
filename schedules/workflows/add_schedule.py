import traceback

from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.integra.schedules import utils


class SetPostDetailsAction(workflows.Action):

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

    priority = forms.IntegerField(
        label=_("Priority"),
        required=True,
        min_value=1,
        max_value=10000,
        help_text=_("Priority"))

    enabled = forms.BooleanField(
        label=_("Enabled"),
        required=False,
        help_text=_("Enabled"))

    class Meta:
        name = _("Details")

    def __init__(self, request, context, *args, **kwargs):
        self.request = request
        self.context = context
        super(SetPostDetailsAction, self).__init__(
            request, context, *args, **kwargs)

class SetPostDetails(workflows.Step):
    action_class = SetPostDetailsAction
    contributes = ("name", "description", "priority", "enabled")

    def contribute(self, data, context):
        if data:
            context['name'] = data.get("name", "")
            context['description'] = data.get("description", "")
            context['priority'] = data.get("priority", "")
            context['enabled'] = data.get("enabled", "")
        return context


# =====
# Create the post
# =====

class AddSchedule(workflows.Workflow):
    slug = "add"
    name = _("Add")
    finalize_button_name = _("Add")
    success_message = _('Added schedule "%s".')
    failure_message = _('Unable to add schedule "%s".')
    success_url = "horizon:integra:schedules:index"
    failure_url = "horizon:integra:schedules:index"
    default_steps = (SetPostDetails,)

    def format_status_message(self, message):
         return message % self.context.get('name', 'unknown post')

    def handle(self, request, context):
        try:
            for k, v in context.items():
                print(k, v)
                print("-----------------")
            print("===================")

            utils.addSchedule(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to add schedule"))
            return False
