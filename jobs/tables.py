from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard.dashboards.integra.jobs import utils

class DeleteTableData(tables.DeleteAction):
    data_type_singular = _("Job")
    data_type_plural = _("Jobs")

    def delete(self, request, obj_id):
        utils.deleteJob(self, obj_id)

class FilterAction(tables.FilterAction):
    def filter(self, table, posts, filter_string):
        filterString = filter_string.lower()
        return [post for post in posts
                if filterString in post.title.lower()]

class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, post_id):
        pass

class JobsTable(tables.DataTable):
    id = tables.Column("id",
                          verbose_name=_("Id"))

    transaction = tables.Column("transaction",
                          verbose_name=_("Transaction"))

    status = tables.Column("status",
                          verbose_name=_("Status"))

    started = tables.Column("started",
                          verbose_name=_("Started"))

    completed = tables.Column("completed",
                          verbose_name=_("Completed"))

    class Meta:
        name = "integra"
        verbose_name = _("Jobs")
        #status_columns = ["status"]
        row_class = UpdateRow
        table_actions = (FilterAction,)
        row_actions = (DeleteTableData,)
