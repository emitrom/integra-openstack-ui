import traceback
from requests.auth import HTTPBasicAuth

from django.utils.translation import ugettext_lazy as _
import requests

from horizon import exceptions

requests.packages.urllib3.disable_warnings()

integra_url = "https://localhost:8443/rest"
json_headers = {'Accept': 'application/json'}

class Action:
    """
    Action data
    """

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class ProviderAction:
    """
    Provider data
    """

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

def getActions(self):
    try:

        r = requests.get(integra_url + "/workflow_actions", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

        actions = []
        for action in r.json()['workflowActions']:
            actions.append(Action(action[u'id'], action[u'name'], action[u'description']))

        return actions

    except:
        exceptions.handle(self.request,
                          _('Unable to retrieve list of posts.'))
        return []

def getProviderActions(self):
    try:

        r = requests.get(integra_url + "/provider_actions/1", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

        providerActions = []
        for providerAction in r.json()['providerActions']:
            providerActions.append(ProviderAction(providerAction[u'id'], providerAction[u'name'], providerAction[u'description']))

        return providerActions

    except:
        exceptions.handle(self.request,
                          _('Unable to retrieve list of posts.'))
        return []

def getProviders(self):
    try:

        r = requests.get(integra_url + "/providers", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

        providers = []
        for provider in r.json()['providers']:
            providers.append(ProviderAction(provider[u'id'], provider[u'name'], provider[u'description']))
        #for provider in r.json()['providers']:
        #    providers.append(provider)

        return providers

    except:
        exceptions.handle(self.request,
                          _('Unable to retrieve list of posts.'))
        return []
# request - horizon environment settings
# context - user inputs from form
def addAction(self, request, context):
    try:

        name = context.get('name')
        description = context.get('description')
        action = context.get('action')

        payload = {'name': name, 'description': description}
        requests.post(integra_url + "/workflow_actions", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.addWorkflow"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to add workflow'))
        return []

# id is required for table
def deleteAction(self, actionId):
    try:

        requests.delete(integra_url + "/workflow_actions/" + actionId, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.deleteWorkflow"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete workflow'))
        return False
