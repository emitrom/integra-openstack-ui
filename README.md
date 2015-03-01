# integra-openstack-ui installation steps

1) Install Integra Python SDK
https://github.com/emitrom/integra-sdk-python

or

pip install integra-sdk

2) Add file horizon/openstack_dashboard/enabled/_50_integra.py

DASHBOARD = 'integra'

DISABLED = False

ADD_INSTALLED_APPS = [
    'openstack_dashboard.dashboards.integra',
]

3) git clone this repo to horizon/openstack_dashboard/dashboards/integra

4) add following line to end of the requirements.txt file under horizon directory

integra-sdk>=0.1.1 # Apache 2 License

5) from horizon directiony run
./run_tests.sh --runserver 0.0.0.0:8877

6) connect to openstack http://yourIP:8877
