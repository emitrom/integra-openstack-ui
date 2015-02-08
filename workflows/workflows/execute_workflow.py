import traceback

from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.integra.workflows import utils


class ExecuteWorkflowAction(workflows.Action):
    scheduleId = forms.IntegerField(
        label=_("WorkflowId)"),
        required=True,
        min_value=1,
        max_value=9999999,
        help_text=_("WorkflowId"))

    class Meta:
        name = _("Execute Details")

    def __init__(self, request, context, *args, **kwargs):
        self.request = request
        self.context = context
        super(ExecuteWorkflowAction, self).__init__(
            request, context, *args, **kwargs)

class ExecuteWorkflowDetails(workflows.Step):
    action_class = ExecuteWorkflowAction
    contributes = ("workflowId", )

    def contribute(self, data, context):
        if data:
            context['workflowId'] = data.get("workflowId", "")
        return context


# =====
# Create the post
# =====

class ExecuteWorkflow(workflows.Workflow):
    slug = "execute"
    name = _("Execute")
    finalize_button_name = _("Execute")
    success_message = _('Execute workflow "%s".')
    failure_message = _('Unable to execute workflow "%s".')
    success_url = "horizon:integra:workflows:index"
    failure_url = "horizon:integra:workflows:index"
    default_steps = (ExecuteWorkflowDetails,)

    def format_status_message(self, message):
         return message % self.context.get('name', 'unknown workflow')

    def handle(self, request, context):
        try:
            for k, v in context.items():
                print(k, v)
                print("-----------------")
            print("===================")

            utils.executeWorkflow(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to execute workflow"))
            return False
