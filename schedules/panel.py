from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Schedules(horizon.Panel):
    name = _("Schedules")
    slug = "schedules"


dashboard.Integra.register(Schedules)
