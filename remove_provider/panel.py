from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Remove_Provider(horizon.Panel):
    name = _("Remove_Provider")
    slug = "remove_provider"


dashboard.Integra.register(Remove_Provider)
