#!/usr/bin/env python3
import subprocess
import sys
import re

"""
Roda os scripts:
  - dnsrecon.py
  - portscan.py
  - BFDirComuns.py

Param1: Dominio 
  Ex: google.com
"""

domain = sys.argv[1]

def getDnsDict(stdout):
    dns_dict = {}
    
    pattern = re.compile(r'Subdominio encontrado:\s+([^\s]+)\s+:\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)') # Expressão regular para encontrar domínios e IPs
    matches = pattern.findall(stdout)

    for dominio, ip in matches:
        dns_dict[dominio] = ip
    
    return dns_dict

def script():
    print(f'\n--- Iniciando DNS recon - {domain} ---\n')
    res = subprocess.run(f'python3 dnsrecon.py {domain}', check=False, shell=True, text=True, capture_output=True)
    print(res.stdout)

    dns_dict = getDnsDict(res.stdout)

    print(f'\n--- Iniciando Port Scan ---\n')
    for currentDomain, currentIp in dns_dict.items():
      print(f'\nIniciando Port Scan - {currentDomain}')
      subprocess.run(f'python3 portscan.py {currentIp}', check=False, shell=True)
    
    print(f'\n--- Iniciando Brute Force Directory - {domain} ---\n')
    subprocess.run(f'python3 BFDirComuns.py {domain}', check=False, shell=True)

def main():
    script()

if __name__ == '__main__':
    main()