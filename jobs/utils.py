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

class Job:
    """
    Job data
    """

    def __init__(self, id, transaction, status, started, completed):
        self.id = id
        self.transaction = transaction
        self.status = status
        self.started = started
        self.completed = completed

def getJobs(self):
    try:
        r = requests.get(integra_url + "/schedules_results", verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

        jobs = []
        for job in r.json()['scheduleResults']:
            jobs.append(Job(job[u'id'], job[u'transaction'], job[u'status'], job[u'started'], job[u'completed']))

        return jobs

    except:
        exceptions.handle(self.request,
                          _('Unable to get jobs'))
        return []

# id is required for table
def deleteJob(self, post_id):
    try:

        requests.delete(integra_url + "/schedules_results/" + post_id, verify=False, auth=HTTPBasicAuth('admin', 'integra'), headers=json_headers)

    except:
        print "Exception inside utils.deleteJob"
        print traceback.format_exc()
        exceptions.handle(self.request,
                          _('Unable to delete job'))
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
