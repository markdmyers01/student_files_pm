"""

    01_server.py
    A basic (featureless) server that uses sockets to receive client requests.

"""
import socket
import sys

port = 8501
connection_queue = 3
server = socket.gethostname()

try:
    with socket.socket() as sock:
        sock.bind((server, port))                        # bind to a local address
        sock.listen(connection_queue)                    # num connections to allow (queue) before refusing
        print(f'Server running on port {port}')
        while True:
            try:
                client_conn, client_address = sock.accept()  # wait for an incoming connection, returns client connection and client address
                print('Client connected: ', client_address)
                with client_conn:
                    client_conn.sendall(b'Welcome to my server!')
            except socket.error as err:
                print('Error communicating with client.')
                print(f'{err}', file=sys.stderr)
                sys.exit()
except socket.error as err:
    print(f'Error binding socket to server: {err}', file=sys.stderr)
    print('Is your server already running?', file=sys.stderr)
    sys.exit()
