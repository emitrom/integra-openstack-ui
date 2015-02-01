from django import template
from django.template.defaultfilters import filesizeformat, time
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import tables  #, workflows, forms

from openstack_dashboard.dashboards.integra.providers import utils


class CreatePost(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Post")
    url = "horizon:integra:providers:create"
    classes = ("btn-launch", "ajax-modal")

class DeletePost(tables.DeleteAction):
    data_type_singular = _("Post")
    data_type_plural = _("Posts")

    def delete(self, request, obj_id):
        utils.delete_post(self, obj_id)

class PostFilterAction(tables.FilterAction):
    def filter(self, table, posts, filter_string):
        """Naive case-insensitive search."""
        filterString = filter_string.lower()
        return [post for post in posts
                if filterString in post.title.lower()]

class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, post_id):
        pass

class PostsTable(tables.DataTable):

    STATUS_CHOICES=(
        ('draft', True),
        ('pending', True),
        ('private', True),
        ('publish', True),
    )

    STATUS_DISPLAY_CHOICES=(
        ('Draft', _('Draft')),
        ('Pending', _('Pending')),
        ('Private', _('Private')),
        ('Publish', _('Publish')),
    )

    title = tables.Column("post_title",
                          verbose_name=_("Post Title"))

    date = tables.Column("post_date",
                           verbose_name=_("Date"))#,
                           #filters=(utils.parse_time,),
                           #attrs={'data-type': 'datetime'}
                           #)

    status = tables.Column("post_status",
                          verbose_name=_("Status"))#,
                          #status=True,
                          #status_choices=STATUS_CHOICES,
                          #display_choices=STATUS_DISPLAY_CHOICES)

    class Meta:
        name = "integra"
        verbose_name = _("Posts BLA")
        status_columns = ["status"]
        #row_class = UpdateRow
        table_actions = (CreatePost,
                         PostFilterAction)
        row_actions = (DeletePost,)
