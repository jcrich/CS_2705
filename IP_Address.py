import ipaddress

def user_input():
    ip_addr = ipaddress.ip_network(input("Please enter a valid IPv4 or IPv6 address in CIDR notation: "))
    return ip_addr

def address_type(ip_addr):
    if ip_addr.is_multicast:
        return "multicast"
    elif ip_addr.is_loopback:
        return "loopback"
    elif ip_addr.is_reserved:
        return "reserved"
    elif ip_addr.is_unspecified:
        return "unspecified"
    elif ip_addr.is_private:
        return "private"
    else:
        return "global"

def network_address(ip_addr):
    return ip_addr.network_address

def no_of_addr(ip_addr):
    return ip_addr.num_addresses

def no_of_usable(no_of_addr):
    return no_of_addr - 2

def broadcast_addr(ip_addr):
    return ip_addr.broadcast_address

def address_info():
    ip_addr = user_input()
    number_of_addr = no_of_addr(ip_addr)
    
    print("The IP address", ip_addr, "is a", address_type(ip_addr), "address.")
    print("It is part of the", network_address(ip_addr), "network.")
    print("This network has", number_of_addr, "addresses of which", no_of_usable(no_of_addr(ip_addr)), "addresses are usable.")
    print("The broadcast address for this network is", broadcast_addr(ip_addr))
    if number_of_addr < 32:
        print("The usable addresses are:")
        for addr in ip_addr.hosts():
            print(addr)
        
if __name__ == '__main__':
    address_info()
