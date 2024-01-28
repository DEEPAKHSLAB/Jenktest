from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result as np

nr = InitNornir(config_file="config.yaml")

def set_snmp(task):
    task.run(task=netmiko_send_config, config_commands=[f"set snmp community {task.host['snmp']}","commit"])

np(nr.run(task=set_snmp))