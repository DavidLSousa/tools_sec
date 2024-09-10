#!/usr/bin/env python3
import socket
import sys

domain = sys.argv[1]

subdominios = (
  'www','mail','webmail','ftp','admin','api','blog','dev','staging','test','shop','store','forum','help','support','docs','images','video','news','static','cdn','assets','media','download','portal','secure','remote','status','dashboard','internal','private','vpn','cloud','services','user','accounts','profile','login','register','signup','newsletter','feedback','survey','marketing','events','conference','partners','affiliates','promo','sales','offers','billing','invoice','payment','checkout','demo','beta','alpha','sandbox','devops','monitor','logs','metrics','alerts','search','discover','api-docs','gateway','auth','sso','identity','backup','cluster','node','repo','git','ci','cd','ci-cd','integration','qa','prod','mirror','dist','release'
)

def dnsrecon(subdomains):
  for subdomain in subdomains:
    subdomainUrl = f'{subdomain}.{domain}'

    try:
      ip = socket.gethostbyname(subdomainUrl)
      print(f'Subdominio encontrado: {subdomainUrl} : {ip}')
    except:
      pass

def main():
  dnsrecon(subdominios)

if __name__ == '__main__':
    main()
