import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address, port = input("Please enter a host and port number, separated by a space: ").split()
    dest_address = (address, int(port))
    quote_request(sock, dest_address)

def quote_request(_sock, _addr):
    qotd_request = "Please send me a quote"
    _sock.sendto(qotd_request.encode('ascii'), _addr)
    data, address = _sock.recvfrom(4096)
    print("The QOTD from", address[0], "is", data.decode('ascii'))

    num = int(input("\nInput 1, 2, or 3, then press enter:\n1 - Request another quote from the same server\n2 - Enter a different host address and/or port number\n3 - Terminate session \n"))
    if num == 1:
        quote_request(_sock, _addr)
    elif num == 2:
        main()
    else:
        _sock.close()

if __name__ == '__main__':
    main()
