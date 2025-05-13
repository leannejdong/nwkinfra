from ip_calculator import from_ip_and_subnet, from_network_address

result = from_ip_and_subnet("192.168.1.10", "255.255.255.0")
print(result["network_address"])

result2 = from_network_address("192.168.1.0/24")
print(result2["sample_ip"])

