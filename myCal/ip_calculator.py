import ipaddress

def from_ip_and_subnet(ip_str, subnet_mask_str):
    ip = ipaddress.IPv4Address(ip_str)
    mask = ipaddress.IPv4Address(subnet_mask_str)
    mask_bin = bin(int(mask))[2:].zfill(32)
    cidr = mask_bin.count('1')
    network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)
    hosts = list(network.hosts())

    return {
        "input_ip": ip_str,
        "subnet_mask": subnet_mask_str,
        "cidr": cidr,
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "first_host": str(hosts[0]) if hosts else "N/A",
        "last_host": str(hosts[-1]) if hosts else "N/A",
        "host_bits": 32 - cidr,
        "usable_hosts": len(hosts)
    }

def from_network_address(cidr_notation):
    network = ipaddress.IPv4Network(cidr_notation, strict=False)
    hosts = list(network.hosts())

    return {
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "first_host": str(hosts[0]) if hosts else "N/A",
        "last_host": str(hosts[-1]) if hosts else "N/A",
        "cidr": network.prefixlen,
        "host_bits": 32 - network.prefixlen,
        "usable_hosts": len(hosts),
        "sample_ip": str(hosts[len(hosts)//2]) if hosts else "N/A"
    }

# Example usage
if __name__ == "__main__":
    print("From IP + Subnet Mask:")
    info1 = from_ip_and_subnet("172.30.239.145", "255.255.192.0")
    for key, val in info1.items():
        print(f"{key.replace('_',' ').title()}: {val}")

    print("\nFrom Network Address (CIDR):")
    info2 = from_network_address("172.30.192.0/18")
    for key, val in info2.items():
        print(f"{key.replace('_',' ').title()}: {val}")

