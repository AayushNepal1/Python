ip = []

# Making the 30 subnets of the ip address

for host in range(30):
    address = {'vendor': 'cisco', 'model': 'iosv', 'ip_address': '10.1.1.1'}
    ip.append(address)

# Now changing the 3 vendors 
for ipv4 in ip[:3]:
    if ipv4['vendor'] == 'cisco':
        ipv4['vendor'] = 'arista'
        ipv4['model'] = 'eos',
        ipv4['ip_address'] = '10.0.0.1'
    # If vendor replace the device from the cisco - arista then the device will repalce it's vendor to arista
    elif ipv4['vendor'] == 'arista':
        ipv4['vendor'] = 'juniper'
        ipv4['model'] = 'junos'
        ipv4['ip_address'] = '10.10.1.1'

    # Now printing the iterables
    
    for key, value in address.items():
        print(f"{key}: {value}")
    print("............")
print()

# Printing the five ip address 
for ipv4 in ip[:5]:
    print(ipv4)
print(":...:")
 
# To print how many host are available in the network
print(f"There are {len(ip)} host up in your network.")

