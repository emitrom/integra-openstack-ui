from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Providers(horizon.Panel):
    name = _("Providers")
    slug = "providers"


dashboard.Integra.register(Providers)
