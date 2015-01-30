from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Remove_Workflow(horizon.Panel):
    name = _("Remove_Workflow")
    slug = "remove_workflow"


dashboard.Integra.register(Remove_Workflow)
