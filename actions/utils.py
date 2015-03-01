import traceback
from integra.RestTemplate import RestTemplate

from requests.auth import HTTPBasicAuth

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
import requests
from integra.integra import workflowAction, provider

from horizon import exceptions


requests.packages.urllib3.disable_warnings()

integra_url = "https://localhost:8443/rest"
json_headers = {'Accept': 'application/json'}
RestTemplate().init('https://localhost:8443/rest', 'admin', 'integra')
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
        provider_actions = RestTemplate().get_all(RestTemplate.PROVIDER_ACTIONS + "/1")
        return provider_actions.providerAction

    except:
        exceptions.handle(self.request,
                          _('Unable to retrieve list of posts.'))
        return []

def getProviders(self):
    try:
        provider_list = RestTemplate().get_all(RestTemplate.PROVIDERS)

        return provider_list.provider

    except:
        exceptions.handle(self.request,
                          _('Unable to retrieve list of posts.'))
        return []
# request - horizon environment settings
# context - user inputs from form
def addAction(self, request, context):
    try:

        #name = context.get('name')
        #description = context.get('description')
        #action = context.get('action')

        #payload = {'name': name, 'description': description}
        #requests.post(integra_url + "/workflow_actions", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

        workflow_action = workflowAction()
        provider = RestTemplate().get_by_id(RestTemplate.PROVIDERS, '1')
        provider_action = RestTemplate().get_by_id(RestTemplate.WORKFLOW_ACTIONS, '1')
        workflow_action.set_name(context.get('name'))
        workflow_action.set_description(context.get('description'))
        workflow_action.set_provider(provider)
        workflow_action.set_providerAction(provider_action)
        RestTemplate().post(RestTemplate.WORKFLOW_ACTIONS, workflow_action)
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
