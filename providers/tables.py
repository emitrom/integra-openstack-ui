from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard.dashboards.integra.providers import utils


class CreatePost(tables.LinkAction):
    name = "add"
    verbose_name = _("Add Provider")
    url = "horizon:integra:providers:create"
    classes = ("btn-launch", "ajax-modal")

class DeletePost(tables.DeleteAction):
    data_type_singular = _("Provider")
    data_type_plural = _("Providers")

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

    name = tables.Column("name",
                          verbose_name=_("Name"))

    description = tables.Column("description",
                          verbose_name=_("Description"))

    class Meta:
        name = "integra"
        verbose_name = _("Providers")
        #status_columns = ["status"]
        row_class = UpdateRow
        table_actions = (CreatePost,
                         PostFilterAction)
        row_actions = (DeletePost,)
