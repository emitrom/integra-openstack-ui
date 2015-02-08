from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Actions(horizon.Panel):
    name = _("Actions")
    slug = "actions"

dashboard.Integra.register(Actions)
