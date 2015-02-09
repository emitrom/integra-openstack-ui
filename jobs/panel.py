from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Jobs(horizon.Panel):
    name = _("Jobs")
    slug = "jobs"


dashboard.Integra.register(Jobs)
