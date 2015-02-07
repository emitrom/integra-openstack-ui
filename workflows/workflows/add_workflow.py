import traceback

from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.integra.workflows import utils


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

    class Meta:
        name = _("Details")

    def __init__(self, request, context, *args, **kwargs):
        self.request = request
        self.context = context
        super(SetPostDetailsAction, self).__init__(
            request, context, *args, **kwargs)

class SetPostDetails(workflows.Step):
    action_class = SetPostDetailsAction
    contributes = ("name", "description")

    def contribute(self, data, context):
        if data:
            context['name'] = data.get("name", "")
            context['description'] = data.get("description", "")
        return context


# =====
# Create the post
# =====

class AddWorkflow(workflows.Workflow):
    slug = "add"
    name = _("Add")
    finalize_button_name = _("Add")
    success_message = _('Added workflow "%s".')
    failure_message = _('Unable to add provider "%s".')
    success_url = "horizon:integra:workflows:index"
    failure_url = "horizon:integra:workflows:index"
    default_steps = (SetPostDetails,)

    def format_status_message(self, message):
         return message % self.context.get('name', 'unknown workflow')

    def handle(self, request, context):
        try:
            for k, v in context.items():
                print(k, v)
                print("-----------------")
            print("===================")

            utils.addWorkflow(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to add workflow"))
            return False
