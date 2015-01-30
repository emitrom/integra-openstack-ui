from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class ListProviders(horizon.Panel):
    name = _("ListProviders")
    slug = "list_providers"


dashboard.Integra.register(ListProviders)
