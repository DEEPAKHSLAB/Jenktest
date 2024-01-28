from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result as np

nr = InitNornir(config_file="config.yaml")

def gather_data(task):
    task.run(task=napalm_get, getters=["get_interfaces_ip"])

result = nr.run(task=gather_data)

np(result)
