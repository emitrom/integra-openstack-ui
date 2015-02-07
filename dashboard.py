from django.utils.translation import ugettext_lazy as _

import horizon


class Providers(horizon.PanelGroup):
    slug = "providers"
    name = _("Providers")
    panels = ('providers',)

class Workflows(horizon.PanelGroup):
    slug = "workflows"
    name = _("Workflows")
    panels = ('workflows',)

class Schedules(horizon.PanelGroup):
    slug = "schedules"
    name = _("Schedules")
    panels = ('schedules',)

class Integra(horizon.Dashboard):
    name = _("Integra")
    slug = "integra"
    panels = (Providers, Workflows, Schedules)  # Add your panels here.
    default_panel = 'providers'  # Specify the slug of the default panel.


horizon.register(Integra)
