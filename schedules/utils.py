import traceback
from requests.auth import HTTPBasicAuth

from django.utils.translation import ugettext_lazy as _
import requests

from horizon import exceptions


requests.packages.urllib3.disable_warnings()

integra_url = "https://localhost:8443/rest"
json_headers = {'Accept': 'application/json'}

class Provider:
    """
    Schedule data
    """

    def __init__(self, id, name, description, priority, enabled):
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority
        self.enabled = enabled

def getSchedules(self):
    try:
        r = requests.get(integra_url + "/schedules", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

        schedules = []
        for schedule in r.json()['schedules']:
            schedules.append(Provider(schedule[u'id'], schedule[u'name'], schedule[u'description'], schedule[u'priority'], schedule[u'enabled']))

        return schedules

    except:
        exceptions.handle(self.request,
                          _('Unable to get schedules'))
        return []

# request - horizon environment settings
# context - user inputs from form
def addSchedule(self, request, context):
    try:

        name = context.get('name')
        description = context.get('description')
        priority = context.get('priority')
        enabled = context.get('enabled')

        payload = {'name': name, 'description': description, 'priority': priority, 'enabled': enabled}
        requests.post(integra_url + "/schedules", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.addSchedule"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to add schedule'))
        return []

# id is required for table
def deleteSchedule(self, post_id):
    try:

        requests.delete(integra_url + "/schedules/" + post_id, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.deleteSchedule"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete schedule'))
        return False
