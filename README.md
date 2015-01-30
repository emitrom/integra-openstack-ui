# integra-openstack-ui

1) Add file horizon/openstack_dashboard_enabled/_50_integra.py

### The name of the dashboard to be added to HORIZON['dashboards']. Required.
DASHBOARD = 'integra'

### If set to True, this dashboard will not be added to the settings.
DISABLED = False

### A list of applications to be added to INSTALLED_APPS.
ADD_INSTALLED_APPS = [
    'openstack_dashboard.dashboards.integra',
]

2) from horizon directiony run
./run_tests.sh --runserver 0.0.0.0:8877

3) connect to openstack http://<your ip>:8877
