from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class ListSchedules(horizon.Panel):
    name = _("ListSchedules")
    slug = "list_schedules"


dashboard.Integra.register(ListSchedules)
