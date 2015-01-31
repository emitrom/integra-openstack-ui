from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.integra import dashboard

class PostsPanel(horizon.Panel):
    name = _("Posts")
    slug = 'wp'

dashboard.Integra.register(PostsPanel)

