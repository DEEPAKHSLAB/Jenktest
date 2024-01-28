from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result as np

nr = InitNornir(config_file="config.yaml")

def config_snmp(task):
    task.run(task=napalm_configure, configuration="set snmp community NORNIR-NAPALM-REVERT", revert_in=60)

result = nr.run(task=config_snmp)

np(result)
