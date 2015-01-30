from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Add_Provider(horizon.Panel):
    name = _("Add_Provider")
    slug = "add_provider"


dashboard.Integra.register(Add_Provider)
