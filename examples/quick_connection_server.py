import socket;

LOCAL_HOST = "192.168.1.11";
LOCAL_PORT = 8080;

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((LOCAL_HOST, LOCAL_PORT))
# become a server socket
serversocket.listen(5);

while True:
    print('waiting for a connection')
    connection, client_address = serversocket.accept()
    try:
        print('client connected:', client_address)
        while True:
            try:
                data = connection.recv(16)
            except ConnectionResetError:
                print('client reset by peer')
            except BrokenPipeError:
                print('broken pipe')
            print('received {!r}'.format(data))
            if data:
                try:
                    connection.sendall(data)
                except BrokenPipeError:
                    print('broken pipe')
            else:
                break
    finally:
        connection.close()