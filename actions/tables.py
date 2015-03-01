from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard.dashboards.integra.actions import utils


class AddTableData(tables.LinkAction):
    name = "add"
    verbose_name = _("Add Action")
    url = "horizon:integra:actions:create"
    classes = ("btn-launch", "ajax-modal")

class DeleteTableData(tables.DeleteAction):
    data_type_singular = _("Action")
    data_type_plural = _("Actions")

    def delete(self, request, obj_id):
        utils.deleteAction(self, obj_id)

class FilterAction(tables.FilterAction):
    def filter(self, table, posts, filter_string):
        """Naive case-insensitive search."""
        filterString = filter_string.lower()
        return [post for post in posts
                if filterString in post.title.lower()]

class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, post_id):
        pass

class ActionTable(tables.DataTable):

    id = tables.Column("id",
                          verbose_name=_("Id"))

    name = tables.Column("name",
                          verbose_name=_("Name"))

    description = tables.Column("description",
                          verbose_name=_("Description"))

    class Meta:
        name = "integra"
        verbose_name = _("Actions")
        row_class = UpdateRow
        table_actions = (AddTableData,
                         FilterAction)
        row_actions = (DeleteTableData,)
