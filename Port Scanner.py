from ipaddress import ip_address
from multiprocessing import connection
import socket

ip_addr = input (" Enter IP address to scan: ")
portrange = input(" Enter a range of port numbers(ie. 1-10): ")

min_port = int(portrange.split ("-")[0])
max_port = int(portrange.split ("-")[1])

print (" Scanning IP ", ip_addr, "from ports", min_port, "-", max_port )

for port in range(min_port,max_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan_res = sock.connect_ex((ip_addr , port))
    if scan_res == 0:
        print ("!! Port " + str(port) + " - OPEN !!")
    else:
        print (" Port " + str(port) + " - CLOSED")
    sock.close()
