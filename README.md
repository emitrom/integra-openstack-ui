# integra-openstack-ui installation steps

1) Add file horizon/openstack_dashboard/enabled/_50_integra.py

DASHBOARD = 'integra'

DISABLED = False

ADD_INSTALLED_APPS = [
    'openstack_dashboard.dashboards.integra',
]

2) git clone this repo to horizon/openstack_dashboard/dashboards/integra

3) from horizon directiony run
./run_tests.sh --runserver 0.0.0.0:8877

4) connect to openstack http://yourIP:8877
