from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.integra import dashboard

class Add_Workflow(horizon.Panel):
    name = _("Add_Workflow")
    slug = "add_workflow"


dashboard.Integra.register(Add_Workflow)
