from django.utils.translation import ugettext_lazy as _

import horizon


class Mygroup(horizon.PanelGroup):
    slug = "mygroup"
    name = _("My Group")
    panels = ('mypanel',)


class Integra(horizon.Dashboard):
    name = _("Integra")
    slug = "integra"
    panels = (Mygroup,)  # Add your panels here.
    default_panel = 'mypanel'  # Specify the slug of the default panel.


horizon.register(Integra)
