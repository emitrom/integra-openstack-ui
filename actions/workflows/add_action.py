import traceback

from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.integra.actions import utils
from django.template.defaultfilters import filesizeformat
import requests
requests.packages.urllib3.disable_warnings()

class SetAddDetailsAction(workflows.Action):


    providerActions = utils.getProviderActions(requests)
    providers = utils.getProviders(requests)

    # providerChoices = [('', '-- Provider Actions --'), ] + [(providerAction.id, providerAction.name) for providerAction in providerActions]
    providerActionsChoices = [(providerAction.id, providerAction.name) for providerAction in providerActions]
    providerChoices = [(provider.id, provider.name) for provider in providers]

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

    provider = forms.ChoiceField(
        label=_("Providers"),
        choices=providerChoices,
        required=True,
        help_text=_("Providers"))

    action = forms.ChoiceField(
        label=_("Provider Actions"),
        choices=providerActionsChoices,
        required=True,
        help_text=_("Provider Actions"))


    #image_id = forms.ChoiceField(
    #    label=_("Image Name"),
    #    required=False,
    #    widget=forms.SelectWidget(
    #        data_attrs=('volume_size',),
    #        transform=lambda action: ("%s (%s)" % (action.id,action.name))))


    class Meta:
        name = _("Details")

    def __init__(self, request, context, *args, **kwargs):
        self.request = request
        self.context = context
        super(SetAddDetailsAction, self).__init__(
            request, context, *args, **kwargs)

class SetAddDetails(workflows.Step):
    action_class = SetAddDetailsAction
    contributes = ("name", "description", "action", "provider")

    def contribute(self, data, context):
        if data:
            context['name'] = data.get("name", "")
            context['description'] = data.get("description", "")
            context['action'] = data.get("action", "")
            context['provider'] = data.get("provider", "")
        return context

class AddAction(workflows.Workflow):
    slug = "add"
    name = _("Add")
    finalize_button_name = _("Add")
    success_message = _('Added action "%s".')
    failure_message = _('Unable to add action "%s".')
    success_url = "horizon:integra:actions:index"
    failure_url = "horizon:integra:actions:index"
    default_steps = (SetAddDetails,)

    def format_status_message(self, message):
         return message % self.context.get('name', 'unknown action')

    def handle(self, request, context):
        try:
            for k, v in context.items():
                print(k, v)
                print("-----------------")
            print("===================")

            utils.addAction(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to add action"))
            return False
