from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Remove_Schedule(horizon.Panel):
    name = _("Remove_Schedule")
    slug = "remove_schedule"


dashboard.Integra.register(Remove_Schedule)
