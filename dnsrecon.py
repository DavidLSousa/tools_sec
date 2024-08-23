#!/usr/bin/env python3
import socket
import sys

domain = sys.argv[1]

def dnsrecon():
  with open('/home/davidlsousa/lists/subdominios.txt', 'r') as subdominiosFile:
    subdomains = subdominiosFile.read().splitlines()

    for subdomain in subdomains:
      subdomainUrl = f'{subdomain}.{domain}'

      try:
        ip = socket.gethostbyname(subdomainUrl)
        print(f'Subdominio encontrado: {subdomainUrl} : {ip}')
      except:
        pass

def main():
  dnsrecon()

if __name__ == '__main__':
    main()
