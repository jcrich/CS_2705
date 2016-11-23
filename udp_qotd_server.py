import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(input("Please enter a valid port number: "))
bound_address = ("", port)
sock.bind(bound_address)

while 1:
        
    data, sender_address = sock.recvfrom(4096)

    #Quote of the Day
    rng = random.randint(1,3)
    if rng == 1:
        quote = "\"Do or do not, there is no try.\" - Yoda"
    elif rng == 2:
        quote = "\"Do not take life too seriously. You will never get out of it alive.\" - Elbert Hubbard"
    else:
        quote = "\"An optimist is a person who starts a new diet on Thanksgiving Day.\" - Irv Kupcinet"
    
    #Server response
    response = quote
    sock.sendto(response.encode('ascii'), sender_address)

sock.close()
