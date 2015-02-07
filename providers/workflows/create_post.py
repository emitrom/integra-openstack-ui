import traceback

from horizon import workflows, forms, exceptions
from horizon.utils import validators

from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError  # noqa
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.integra.providers import utils


class SetPostDetailsAction(workflows.Action):

    post_name = forms.CharField(
        label=_("Name"),
        required=True,
        max_length=80,
        help_text=_("Name"))

    post_description = forms.CharField(
        label=_("Description"),
        required=True,
        max_length=120,
        help_text=_("Description"))

    post_hostname = forms.CharField(
        label=_("Hostname"),
        required=True,
        max_length=120,
        help_text=_("Hostname"))

    post_port = forms.IntegerField(
        label=_("Port"),
        required=True,
        min_value=1,
        max_value=65535,
        help_text=_("Port"))

    post_timeout = forms.IntegerField(
        label=_("Timeout"),
        required=True,
        min_value=1,
        max_value=100000,
        help_text=_("Timeout"))

    post_secured = forms.BooleanField(
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
    contributes = ("post_name", "post_description", "post_hostname", "post_port", "post_timeout", "post_secured")

    def contribute(self, data, context):
        if data:
            context['post_name'] = data.get("post_name", "")
            context['post_description'] = data.get("post_description", "")
            context['post_hostname'] = data.get("post_hostname", "")
            context['post_port'] = data.get("post_port", "")
            context['post_timeout'] = data.get("post_timeout", "")
            context['post_secured'] = data.get("post_secured", "")
        return context


# =====
# Create the post
# =====

class CreatePost(workflows.Workflow):
    slug = "add"
    name = _("Add")
    finalize_button_name = _("Add")
    success_message = _('Added provider "%s".')
    failure_message = _('Unable to add provider "%s".')
    success_url = "horizon:integra:providers:index"
    failure_url = "horizon:integra:providers:index"
    default_steps = (SetPostDetails,)

    def format_status_message(self, message):
         return message % self.context.get('post_name', 'unknown post')

    def handle(self, request, context):
        try:
            for k, v in context.items():
                print(k, v)
                print("-----------------")
            print("===================")

            utils.create_post(self, request, context)
            return True
        except Exception:
            print traceback.format_exc()
            exceptions.handle(request, _("Unable to setup post create."))
            return False
