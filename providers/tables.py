from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard.dashboards.integra.providers import utils


class AddTableData(tables.LinkAction):
    name = "add"
    verbose_name = _("Add Provider")
    url = "horizon:integra:providers:add"
    classes = ("btn-launch", "ajax-modal")

class DeleteTableData(tables.DeleteAction):
    data_type_singular = _("Provider")
    data_type_plural = _("Providers")

    def delete(self, request, obj_id):
        utils.deleteProvider(self, obj_id)

class FilterAction(tables.FilterAction):
    def filter(self, table, providers, filter_string):
        filterString = filter_string.lower()
        return [provider for provider in providers
                if filterString in provider.title.lower()]

class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, post_id):
        pass

class ProviderTable(tables.DataTable):
    id = tables.Column("id",
                          verbose_name=_("Id"))

    name = tables.Column("name",
                          verbose_name=_("Name"))

    description = tables.Column("description",
                          verbose_name=_("Description"))

    hostname = tables.Column("hostname",
                          verbose_name=_("Hostname"))

    port = tables.Column("port",
                          verbose_name=_("Port"))

    timeout = tables.Column("timeout",
                          verbose_name=_("Timeout"))

    secured = tables.Column("secured",
                          verbose_name=_("Secured"))

    class Meta:
        name = "integra"
        verbose_name = _("Providers")
        row_class = UpdateRow
        table_actions = (AddTableData,
                         FilterAction)
        row_actions = (DeleteTableData,)
