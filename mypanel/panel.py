from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Mypanel(horizon.Panel):
    name = _("Mypanel")
    slug = "mypanel"


dashboard.Integra.register(Mypanel)
