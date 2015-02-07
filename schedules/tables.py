from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard.dashboards.integra.schedules import utils


class AddTableData(tables.LinkAction):
    name = "add"
    verbose_name = _("Add Schedule")
    url = "horizon:integra:schedules:create"
    classes = ("btn-launch", "ajax-modal")

class DeleteTableData(tables.DeleteAction):
    data_type_singular = _("Schedule")
    data_type_plural = _("Schedule")

    def delete(self, request, obj_id):
        utils.deleteSchedule(self, obj_id)

class FilterAction(tables.FilterAction):
    def filter(self, table, posts, filter_string):
        filterString = filter_string.lower()
        return [post for post in posts
                if filterString in post.title.lower()]

class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, post_id):
        pass

class ScheduleTable(tables.DataTable):

    name = tables.Column("name",
                          verbose_name=_("Name"))

    description = tables.Column("description",
                          verbose_name=_("Description"))

    priority = tables.Column("priority",
                          verbose_name=_("Priority"))

    enabled = tables.Column("enabled",
                          verbose_name=_("Enabled"))

    class Meta:
        name = "integra"
        verbose_name = _("Providers")
        #status_columns = ["status"]
        row_class = UpdateRow
        table_actions = (AddTableData,
                         FilterAction)
        row_actions = (DeleteTableData,)
