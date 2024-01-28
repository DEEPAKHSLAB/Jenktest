from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result as np
from rich import print as rp
import xmltodict


nr = InitNornir(config_file="config.yaml")

def get_some_data(task):
    uptime = task.run(task=netmiko_send_command, command_string="show system uptime | display xml")
    result = xmltodict.parse(uptime.result)
    
    current_time = result["rpc-reply"]["system-uptime-information"]["current-time"]["date-time"]["#text"]
    actual_uptime = result["rpc-reply"]["system-uptime-information"]["uptime-information"]["up-time"]["#text"]
    protocols = result["rpc-reply"]["system-uptime-information"]["protocols-started-time"]["date-time"]["#text"]
    last_configured = result["rpc-reply"]["system-uptime-information"]["last-configured-time"]["date-time"]["#text"]
    rp(f"{task.host}\nCURRENT TIEM: {current_time:>50}\nUPTIME: {actual_uptime:>37}\nPROTOCOLS START TIME: {protocols:>42}\nLAST CONFIGURED AT: {last_configured:>44}\n{'='*55}\n")

nr.run(task=get_some_data)