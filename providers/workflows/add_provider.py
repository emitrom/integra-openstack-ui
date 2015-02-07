import traceback

from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.integra.providers import utils


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

    hostname = forms.CharField(
        label=_("Hostname"),
        required=True,
        max_length=120,
        help_text=_("Hostname"))

    port = forms.IntegerField(
        label=_("Port"),
        required=True,
        min_value=1,
        max_value=65535,
        help_text=_("Port"))

    timeout = forms.IntegerField(
        label=_("Timeout"),
        required=True,
        min_value=1,
        max_value=100000,
        help_text=_("Timeout"))

    secured = forms.BooleanField(
        label=_("Secured"),
        required=False,
        help_text=_("Secured"))

    class Meta:
        name = _("Details")

    def __init__(self, request, context, *args, **kwargs):
        self.request = request
        self.context = context
        super(SetPostDetailsAction, self).__init__(
            request, context, *args, **kwargs)

class SetPostDetails(workflows.Step):
    action_class = SetPostDetailsAction
    contributes = ("name", "description", "hostname", "port", "timeout", "secured")

    def contribute(self, data, context):
        if data:
            context['name'] = data.get("name", "")
            context['description'] = data.get("description", "")
            context['hostname'] = data.get("hostname", "")
            context['port'] = data.get("port", "")
            context['timeout'] = data.get("timeout", "")
            context['secured'] = data.get("secured", "")
        return context


# =====
# Create the post
# =====

class AddProvider(workflows.Workflow):
    slug = "add"
    name = _("Add")
    finalize_button_name = _("Add")
    success_message = _('Added provider "%s".')
    failure_message = _('Unable to add provider "%s".')
    success_url = "horizon:integra:providers:index"
    failure_url = "horizon:integra:providers:index"
    default_steps = (SetPostDetails,)

    def format_status_message(self, message):
         return message % self.context.get('name', 'unknown provider')

    def handle(self, request, context):
        try:
            for k, v in context.items():
                print(k, v)
                print("-----------------")
            print("===================")

            utils.addProvider(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to add provider"))
            return False
