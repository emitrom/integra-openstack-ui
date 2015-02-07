import traceback
import time
from time import mktime
from datetime import datetime
from requests.auth import HTTPBasicAuth

from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
import requests

from horizon import exceptions


requests.packages.urllib3.disable_warnings()

integra_url = "https://localhost:8443/rest"
json_headers = {'Accept': 'application/json'}

class Provider:
    """
    Provider data
    """

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

def getProviders(self):
    try:
        r = requests.get(integra_url + "/providers", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

        providers = []
        for provider in r.json()['providers']:
            print(provider)
            print(provider[u'id'])
            providers.append(Provider(provider[u'id'], provider[u'name'], provider[u'description']))

        return providers

    except:
        exceptions.handle(self.request,
                          _('Unable to get providers'))
        return []

# request - horizon environment settings
# context - user inputs from form
def addProvider(self, request, context):
    try:

        name = context.get('name')
        description = context.get('description')
        hostname = context.get('hostname')
        port = context.get('port')
        timeout = context.get('timeout')
        secured = context.get('secured')

        payload = {'name': name, 'description': description, 'hostname': hostname, 'port': port, 'timeout': timeout, 'secured': secured}
        requests.post(integra_url + "/providers", json=payload, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.addProvider"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to add provider'))
        return []

# id is required for table
def deleteProvider(self, post_id):
    try:

        requests.delete(integra_url + "/providers/" + post_id, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.deleteProvider"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete provider'))
        return False


@register.filter
def parse_time(xmlrpcdt, default=None):
    try:
        struct = time.strptime(str(xmlrpcdt), "%Y%m%dT%H:%M:%S")
        dt = datetime.fromtimestamp(mktime(struct))
        return dt.strftime("%B %d, %Y at %H:%M")
    except Exception:
        print "Exception inside utils.parse_time"
        print traceback.format_exc()
        return default or ''
