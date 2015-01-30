from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class ListWorkflows(horizon.Panel):
    name = _("ListWorkflows")
    slug = "list_workflows"


dashboard.Integra.register(ListWorkflows)
