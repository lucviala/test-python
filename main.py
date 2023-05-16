import socket

def main():

    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    print(IPAddr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 8080))
    sock.listen(1)

    while 1:
        client, clientAddress = sock.accept()
        data = client.recv(1024)
        print('recv')
        print(data)
        print('send')
        client.send(data)
    
    client.close()
    sock.close()

if __name__ == '__main__':
    main()
