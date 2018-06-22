#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from socket import *

# port_scan.py <host> <start_port>-<end_port>

target_ip = gethostbyname('134.70.92.93')#192.168.97.20
opened_ports = []

for port in [21,22, 1522, 3306, 3307,50000]:#
    try:
        sock = socket( AF_INET, SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target_ip, port))
        print(port,"端口开放")
    except Exception:
        continue



print("Opened ports:")

for i in opened_ports:
    print(i)
