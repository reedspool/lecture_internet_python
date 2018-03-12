# From https://docs.python.org/3/howto/sockets.html

import socket;

REMOTE_HOST = "192.168.1.11";
REMOTE_PORT = 8080;

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect((REMOTE_HOST, REMOTE_PORT))
# Now send something
s.sendall(b'Hello world!');