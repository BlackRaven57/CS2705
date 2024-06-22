import ipaddress

ipInterface = ipaddress.ip_interface("192.168.5.12/24")
print(ipInterface)
ipnetwork = ipInterface.network
print(ipnetwork)

print("\n1:")
print("2-bit mask: 255.192.0.0")
print("13-bit mask: 255.255.248.0")
print("5-bit mask: 255.248.0.0")
print("11-bit mask: 255.255.224.0")
print("9-bit mask: 255.255.128.0")
print("10-bit mask: 255.255.192.0")
print("4-bit mask: 255.240.0.0")
print("14-bit mask: 255.255.252.0")
print("6-bit mask: 255.252.0.0")
print("8-bit mask: 255.255.0.0")
print("12-bit mask: 255.255.240.0")

print("\n2:")
ipInterface = ipaddress.ip_interface("132.8.150.67/22")
ipnetwork = ipInterface.network
print("{} is the network address".format(ipaddress.ip_network(ipnetwork).network_address))
print("{} is the broadcast address".format(ipaddress.ip_network(ipnetwork).broadcast_address))
print("{} is the number of total addresses avalible".format(ipaddress.ip_network(ipnetwork).num_addresses))
print("{} is the number of usuable addresses avalible".format((len(list(ipaddress.ip_network(ipnetwork).hosts())))))

print("\n3:")
ipInterface = ipaddress.ip_interface("200.16.5.74/30")
ipnetwork = ipInterface.network
print("{} is the network address".format(ipaddress.ip_network(ipnetwork).network_address))
print("{} is the broadcast address".format(ipaddress.ip_network(ipnetwork).broadcast_address))
print("{} is the number of total addresses avalible".format(ipaddress.ip_network(ipnetwork).num_addresses))
print("{} is the number of usuable addresses avalible".format((len(list(ipaddress.ip_network(ipnetwork).hosts())))))

print("\n4:")
ipInterface = ipaddress.ip_interface("166.0.13.8/22")
ipnetwork = ipInterface.network
print("{} is the network address".format(ipaddress.ip_network(ipnetwork).network_address))
print("{} is the broadcast address".format(ipaddress.ip_network(ipnetwork).broadcast_address))
print("{} is the number of total addresses avalible".format(ipaddress.ip_network(ipnetwork).num_addresses))
print("{} is the number of usuable addresses avalible".format((len(list(ipaddress.ip_network(ipnetwork).hosts())))))

print("\n5:")
ipInterface = ipaddress.ip_interface("166.0.13.8/20")
ipnetwork = ipInterface.network
print("255.255.240.0")
print("12 bits used in this subnet mask")
print("{} is the number of hosts".format((len(list(ipaddress.ip_network(ipnetwork).hosts())))))

print("\n6:")
ipInterface = ipaddress.ip_interface("166.0.13.8/26")
ipnetwork = ipInterface.network
print("255.255.255.192")
print("18 bits used in this subnet mask")
print("{} is the number of hosts".format((len(list(ipaddress.ip_network(ipnetwork).hosts())))))

print("\n7:")
ipInterface = ipaddress.ip_interface("166.0.13.8/22")
ipnetwork = ipInterface.network
print("255.255.252.0")
print("14 bits used in this subnet mask")
print("{} is the number of hosts".format((len(list(ipaddress.ip_network(ipnetwork).hosts())))))

print("\n8:")
ipInterface = ipaddress.ip_interface("166.0.13.8/29")
ipnetwork = ipInterface.network
print("255.255.255.248")
print("21 bits used in this subnet mask")
print("{} is the number of hosts".format((len(list(ipaddress.ip_network(ipnetwork).hosts())))))

print("\n9:")
print("I would use subnet mask 255.255.254.0 that gives you 128 (126) subnets with 510 hosts each.")
