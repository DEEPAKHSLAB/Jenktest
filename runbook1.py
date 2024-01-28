from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from rich import print as rp
from nornir_utils.plugins.functions import print_result as pr

nr = InitNornir(config_file="config.yaml")

def uptime(task):
     task.run(task=netmiko_send_command, command_string="show system uptime")

result = nr.run(task=uptime)
pr(result)
