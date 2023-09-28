"""

    01_client.py
    A basic client that uses sockets to connect to and communicate with a server.

"""
import socket
import sys

sock = None
try:
    with socket.socket() as sock:
        sock.settimeout(5)
        server = socket.gethostname()

        print(f'Connecting to {server}...')
        port = 8501
        sock.connect((server, port))  # IP sockets use (host, port) to connect
        print('Connected...')

        byte_data = sock.recv(1024)  # blocks until data received
        print(byte_data.decode(encoding='utf-8'))
except socket.error as err:
    print(f'Error connecting to server.\n{err}', file=sys.stderr)
    print('Is your server address valid or is the server running?', file=sys.stderr)
    sys.exit()
