import traceback
from requests.auth import HTTPBasicAuth

from django.utils.translation import ugettext_lazy as _
import requests

from horizon import exceptions


requests.packages.urllib3.disable_warnings()

integra_url = "https://localhost:8443/rest"
json_headers = {'Accept': 'application/json'}

class Workflow:
    """
    Workflow data
    """

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

def getWorkflows(self):
    try:

        r = requests.get(integra_url + "/workflows", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

        workflows = []
        for workflow in r.json()['workflows']:
            workflows.append(Workflow(workflow[u'id'], workflow[u'name'], workflow[u'description']))

        return workflows

    except:
        exceptions.handle(self.request,
                          _('Unable to retrieve list of posts.'))
        return []

# request - horizon environment settings
# context - user inputs from form
def addWorkflow(self, request, context):
    try:

        name = context.get('name')
        description = context.get('description')

        payload = {'name': name, 'description': description}
        requests.post(integra_url + "/workflows", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.addWorkflow"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to add workflow'))
        return []

# request - horizon environment settings
# context - user inputs from form
def executeWorkflow(self, request, context):
    try:

        workflowId = context.get('workflowId')
        description = context.get('description')

        url = integra_url + "/workflows/" + workflowId
        requests.post(url, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.executeWorkflow"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to execute workflow'))
        return []

# id is required for table
def deleteWorkflow(self, workflowId):
    try:

        requests.delete(integra_url + "/workflows/" + workflowId, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.deleteWorkflow"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete workflow'))
        return False
