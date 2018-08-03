#!/usr/bin/env python

from netmiko import ConnectHandler
import time

# specify the date and time for use in the filename created on the tftp server
hour=time.strftime('%H')
minute=time.strftime('%M')
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year+"-"+hour+minute

cisco_sg300_01 = { 'device_type':'cisco_s300', 'ip':'XXX.XXX.XXX.XXX', 'username':'admin', 'password':'XXXXXX'}
#cisco_sg300_02 = { 'device_type':'cisco_s300', 'ip':'cisco_sg300_02', 'username':'cisco', 'password':'cisco'}
#cisco_sg300_03 = { 'device_type':'cisco_s300', 'ip':'cisco_sg300_03', 'username':'cisco', 'password':'cisco'}
#cisco_sg300_04 = { 'device_type':'cisco_s300', 'ip':'cisco_sg300_04', 'username':'cisco', 'password':'cisco'}


net_connect = ConnectHandler(**cisco_sg300_01)
result = net_connect.config_mode()  + "\n"
result += net_connect.send_command('do show interface status GigabitEthernet 2')  + "\n"
print result

port_down = ['interface GigabitEthernet 2', 'power inline never']
result = net_connect.send_config_set(port_down) + "\n"
print result

time.sleep(15)

port_auto = ['interface GigabitEthernet 2', 'power inline auto']
result = net_connect.config_mode()  + "\n"
result = net_connect.send_config_set(port_auto, delay_factor=3) + "\n"
print result

net_connect.disconnect()
