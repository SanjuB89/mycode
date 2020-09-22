#!/usr/bin/env python3

import ipaddress

ip = input("Enter ip to validate :: ")
try:
    ipaddress.ip_address(ip)
    print("valid ip")
except ValueError as errorCode:
    print(errorCode)
    print("invalid ip")
