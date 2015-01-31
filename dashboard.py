from django.utils.translation import ugettext_lazy as _

import horizon


class Providers(horizon.PanelGroup):
    slug = "providers"
    name = _("Providers")
    panels = ('list_providers', 'add_provider', 'remove_provider', 'wp')

class Workflows(horizon.PanelGroup):
    slug = "workflows"
    name = _("Workflows")
    panels = ('list_workflows', 'add_workflow', 'remove_workflow')

class Schedules(horizon.PanelGroup):
    slug = "schedules"
    name = _("Schedules")
    panels = ('list_schedules', 'add_schedule', 'remove_schedule')

class Integra(horizon.Dashboard):
    name = _("Integra")
    slug = "integra"
    panels = (Providers, Workflows, Schedules)  # Add your panels here.
    default_panel = 'list_providers'  # Specify the slug of the default panel.


horizon.register(Integra)
