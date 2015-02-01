from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Workflows(horizon.Panel):
    name = _("Workflows")
    slug = "workflows"


dashboard.Integra.register(Workflows)
