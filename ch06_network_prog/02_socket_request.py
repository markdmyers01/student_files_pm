"""
    02_socket_request.py

    A simple socket client that can retrieve a single response from most HTTP servers
    given a proper host and path.

    This solution does not examine HTTP headers (or content for that matter) and therefore
    does not consider content length.
"""

import socket
import ssl

host = 'docs.python.org'
path = '/3/'
port = 443
bufsize = 16384
timeout = 3
request = f'GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\n\r\n'
results = []

context = ssl.create_default_context()
with socket.create_connection((host, port), timeout=timeout) as sock:
    with context.wrap_socket(sock, server_hostname=host) as wrapped_sock:
        wrapped_sock.sendall(request.encode('utf-8'))
        while True:
            try:
                byte_data = wrapped_sock.recv(bufsize)
                results.append(byte_data)
            except socket.timeout:                          # our simple client ignores content-length, so we'll just timeout after 3 secs.
                break

print(b''.join(results).decode('utf-8', errors='ignore'))
