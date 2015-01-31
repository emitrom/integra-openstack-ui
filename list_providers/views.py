
from horizon import tabs

import json
from openstack_dashboard.dashboards.integra.add_provider import tables
from openstack_dashboard.dashboards.integra.list_providers.tables import InstancesTable

class Provider:
    """
    Provider data
    """

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class ProvidersView(tables.tables.DataTableView):
    table_class = InstancesTable
    template_name = 'integra/list_providers/index.html'

    def get_data(self):
        strobj = '[{"id": 1, "name": "plugin", "description": "A plugin provider"}, {"id": 2, "name": "aws", "description": "A amazon web services provider"}]'
        instances = json.loads(strobj)
        ret = []
        for inst in instances:
            ret.append(Provider(inst['id'], inst['name'], inst['description']))
        return ret
