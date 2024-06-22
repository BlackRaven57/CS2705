import ipaddress

#ipType = input("Choose IP Address Type: IPv4 (4) or IPV6 (6): ")
user = ipaddress.ip_address(input("Enter an IP Address: "))

if user.version == 6:
    print("The address you entered is: {}".format(user.exploded))
    print("The address in it's compressed form is: {}".format(user.compressed))
    
else:
    print("The address you entered is: {}".format(user.exploded))
    print("The address in it's binary form is: {}".format(user.packed))

if user.is_private:
    print("This address is a private address")
else:
    print("This address is not a private address")

if user.is_global:
    print("This address is a global address")
else:
    print("This address is not a global address")

if user.is_multicast:
    print("This address is a multicast address")
else:
    print("This address is not a multicast address")
