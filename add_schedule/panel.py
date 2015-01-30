from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Add_Schedule(horizon.Panel):
    name = _("Add_Schedule")
    slug = "add_schedule"


dashboard.Integra.register(Add_Schedule)
