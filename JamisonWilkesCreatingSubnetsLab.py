#JamisonWilkesCreatingSubnetsLab

import ipaddress

#1
ipInterface = ipaddress.ip_interface('192.168.5.0/2')
print('1. 2-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/13')
print('2. 13-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/5')
print('3. 5-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/4')
print('4. 11-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/9')
print('5. 9-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/10')
print('6. 10-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/4')
print('7. 4-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/14')
print('8. 14-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/6')
print('9. 6-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/8')
print('10. 8-bit mask: {}'.format((ipInterface).netmask))
ipInterface = ipaddress.ip_interface('192.168.5.0/12')
print('11. 12-bit mask: {}'.format((ipInterface).netmask))

#2 
print('#2.Use the IP address 132.8.150.67/22 and find the following')
ipInterface = ipaddress.ip_interface('132.8.150.67/22')
ipNetwork = ipInterface.network
print('Network Address: {}'.format((ipNetwork).network_address))
print('Broadcast Address: {}'.format((ipNetwork).broadcast_address))
print('Number of Hosts: {}'.format(len(list((ipNetwork).hosts()))))
print('Valid Host Range: {0} - {1}'.format(((ipNetwork).network_address), (((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

#3
print('3.) Use the IP address 200.16.5.74/30 and find the following')
ipInterface = ipaddress.ip_interface('200.16.5.74/30')
ipNetwork = ipInterface.network
print('Network Address: {}'.format((ipNetwork).network_address))
print('Broadcast Address: {}'.format((ipNetwork).broadcast_address))
print('Number of Hosts: {}'.format(len(list((ipNetwork).hosts()))))
print('Valid Host Range: {0} - {1}'.format(((ipNetwork).network_address), (((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

#4
print('4.) Use the IP address 166.0.13.8 with subnet mask of 255.255.252.0 and find the following')
ipInterface = ipaddress.ip_interface('166.0.13.8/22')
ipNetwork = ipInterface.network
print('Network Address: {}'.format((ipNetwork).network_address))
print('Broadcast Address: {}'.format((ipNetwork).broadcast_address))
print('Number of Hosts: {}'.format(len(list((ipNetwork).hosts()))))
print('Valid Host Range: {0} - {1}'.format(((ipNetwork).network_address), (((ipNetwork).network_address)+1), (((ipNetwork).broadcast_address)-1)))

#5 
print('5.) With this subnet mask 255.255.240.0 answer the following:')
ipInterface = ipaddress.ip_interface('10.10.10.10/255.255.240.0')
ipNetwork = ipInterface.network
print('# of bits used in the subnet mask: {}'.format((ipNetwork).prefixlen))
print('# of hosts: {}'.format(len(list((ipNetwork).hosts()))))

#6
print('6.) With this subnet mask 255.255.255.192 answer the following:')
ipInterface = ipaddress.ip_interface('10.10.10.10/255.255.255.192')
ipNetwork = ipInterface.network
print('# of bits used in the subnet mask: {}'.format((ipNetwork).prefixlen))
print('# of hosts: {}'.format(len(list((ipNetwork).hosts()))))

#7    
print('7.) With this subnet mask 255.255.252.0 answer the following:')
ipInterface = ipaddress.ip_interface('10.10.10.10/255.255.252.0')
ipNetwork = ipInterface.network
print('# of bits used in the subnet mask: {}'.format((ipNetwork).prefixlen))
print('# of hosts: {}'.format(len(list((ipNetwork).hosts()))))  

#8
print('8.) With this subnet mask 255.255.255.248 answer the following:')
ipInterface = ipaddress.ip_interface('10.10.10.10/255.255.255.248')
ipNetwork = ipInterface.network
print('# of bits used in the subnet mask: {}'.format((ipNetwork).prefixlen))
print('# of hosts: {}'.format(len(list((ipNetwork).hosts()))))                               

#9
ipInterface = ipaddress.ip_interface('10.10.10.10/27')
ipNetwork = ipInterface.network
print(ipNetwork)
bitsBorrowed = 3
ipSubnetLength = ipNetwork.prefixlen + bitsBorrowed
print('The subnet mask length is {}'.format(ipSubnetLength))
print('The 7 subnets needed are less than the {} subnets created')
ipSubnet = str('10.10.10.10/') + str(ipSubnetLength)
print(ipSubnet)

