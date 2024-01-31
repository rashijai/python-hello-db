import socket

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.shutdown(socket.SHUT_WR)
    while 1:
        data = s.recv(1024)
        if len(data) == 0:
            break
        print("Received:", repr(data))
    print("Connection closed.")
    s.close()

netcat("google.com", 443)
