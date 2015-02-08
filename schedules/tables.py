from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard.dashboards.integra.schedules import utils
from django.utils.http import urlencode
from django.core.urlresolvers import reverse

class AddTableData(tables.LinkAction):
    name = "addSchedule"
    verbose_name = _("Add Schedule")
    url = "horizon:integra:schedules:create"
    classes = ("btn-launch", "ajax-modal")


class ScheduleTasksData(tables.LinkAction):
    name = "addTask"
    verbose_name = _("Schedule Tasks")
    url = "horizon:integra:schedules:addTask"
    classes = ("btn-launch", "ajax-modal")

    def get_link_url(self, datum):
        base_url = reverse(self.url)

        params = urlencode({"source_id": self.table.get_object_id(datum)})

        return "?".join([base_url, params])


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

    id = tables.Column("id",
                          verbose_name=_("Id"))

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
        verbose_name = _("Schedules")
        #status_columns = ["status"]
        row_class = UpdateRow
        table_actions = (AddTableData,
                         FilterAction)
        row_actions = (DeleteTableData,ScheduleTasksData)
