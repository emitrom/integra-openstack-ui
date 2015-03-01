import traceback
import time
from time import mktime
from datetime import datetime
from integra.RestTemplate import RestTemplate
from integra.integra import provider
from requests.auth import HTTPBasicAuth

from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions

RestTemplate().init('https://localhost:8443/rest', 'admin', 'integra')

def getProviders(self):
    try:
        providers = RestTemplate().get_all(RestTemplate.PROVIDERS)
        return providers.provider

    except:
        exceptions.handle(RestTemplate.PROVIDERS,
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

        prov = provider()
        prov.name = context.get('name')
        prov.description = context.get('description')
        prov.hostname = context.get('hostname')
        prov.port = port = context.get('port')
        prov.timeout = timeout = context.get('timeout')
        prov.secured = context.get('secured')

        RestTemplate().post(RestTemplate.PROVIDERS, prov)

    except:
        print "Exception inside utils.addProvider"
        print traceback.format_exc()
        exceptions.handle(RestTemplate.PROVIDERS,
                          _('Unable to add provider'))
        return []

# id is required for table
def deleteProvider(self, post_id):
    try:
        RestTemplate().delete(RestTemplate.PROVIDERS, post_id)
    except:
        print "Exception inside utils.deleteProvider"
        print traceback.format_exc()
        exceptions.handle(RestTemplate.PROVIDERS,
                          _('Unable to delete provider'))
        return False
