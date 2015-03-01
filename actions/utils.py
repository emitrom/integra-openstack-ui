import traceback
from integra.RestTemplate import RestTemplate

from requests.auth import HTTPBasicAuth
from django.utils.translation import ugettext_lazy as _
from horizon import exceptions
from integra.integra import workflowAction, provider
from horizon import exceptions
import requests


RestTemplate().init('https://localhost:8443/rest', 'admin', 'integra')
requests.packages.urllib3.disable_warnings()

integra_url = "https://localhost:8443/rest"
json_headers = {'Accept': 'application/json'}
def getActions(self):
    try:
        workflow_actions = RestTemplate().get_all(RestTemplate.WORKFLOW_ACTIONS)
        return workflow_actions.workflowAction

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
        #RestTemplate().delete(RestTemplate.WORKFLOW_ACTIONS, 1)
        requests.delete(integra_url + "/workflow_actions/" + actionId, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.deleteWorkflow"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete workflow'))
        return False
