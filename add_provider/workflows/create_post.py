import traceback

from horizon import workflows, forms, exceptions
from horizon.utils import validators

from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError  # noqa
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.integra.add_provider import utils


class SetPostDetailsAction(workflows.Action):

    post_title = forms.CharField(
        label=_("Post Title"),
        required=True,
        max_length=80,
        help_text=_("Enter a title name for your post."))

    post_content = forms.CharField(
        label=_("Content"),
        required=True,
        help_text=_("Enter content for your post."),
        widget = forms.Textarea)

    class Meta:
        name = _("Details")

    def __init__(self, request, context, *args, **kwargs):
        self.request = request
        self.context = context
        super(SetPostDetailsAction, self).__init__(
            request, context, *args, **kwargs)

class SetPostDetails(workflows.Step):
    action_class = SetPostDetailsAction
    contributes = ("post_title", "post_content")

    def contribute(self, data, context):
        if data:
            context['post_title'] = data.get("post_title", "")
            context['post_content'] = data.get("post_content", "")
        return context


# =====
# Create the post
# =====

class CreatePost(workflows.Workflow):
    slug = "create_post"
    name = _("Create Post")
    finalize_button_name = _("Create")
    success_message = _('Created Post named "%s".')
    failure_message = _('Unable to create post named "%s".')
    success_url = "horizon:integra:add_provider:index"
    failure_url = "horizon:integra:add_provider:index"
    default_steps = (SetPostDetails,)

    def format_status_message(self, message):
         return message % self.context.get('post_title', 'unknown post')

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
