#!/usr/bin/env python3
import sys
import socket

ip = sys.argv[1]

ports = (
    '21',   # FTP (File Transfer Protocol)
    '22',   # SSH (Secure Shell)
    '23',   # Telnet
    '25',   # SMTP (Simple Mail Transfer Protocol)
    '53',   # DNS (Domain Name System)
    '80',   # HTTP (Hypertext Transfer Protocol)
    '110',  # POP3 (Post Office Protocol)
    '143',  # IMAP (Internet Message Access Protocol)
    '443',  # HTTPS (HTTP over SSL/TLS)
    '587',  # SMTP (Mail Submission Agent - Encrypted)
    '993',  # IMAP over SSL
    '995',  # POP3 over SSL
    '3306', # MySQL Database
    '3389', # RDP (Remote Desktop Protocol)
    '8080', # HTTP Alternative
    '8443', # HTTPS Alternative
    '135',  # Microsoft RPC (Remote Procedure Call)
    '137',  # NetBIOS Name Service
    '138',  # NetBIOS Datagram Service
    '139',  # NetBIOS Session Service
    '445',  # Microsoft SMB (Server Message Block)
    '1723', # PPTP (Point-to-Point Tunneling Protocol)
    '5900', # VNC (Virtual Network Computing)
    '8081', # HTTP Alternative
    '8888', # HTTP Alternative
    '9000', # Web Applications/Custom Applications
    '1433', # Microsoft SQL Server
    '1521', # Oracle Database
    '2049', # NFS (Network File System)
    '5060', # SIP (Session Initiation Protocol - VoIP)
    '8000', # HTTP Alternative
    '10000',# Webmin (System Administration Interface)
    '49152', '49153', '49154', '49155', '49156', '49157', '49158', '49159', '49160', 
    '49161', '49162', '49163', '49164', '49165', '49166', '49167', '49168', '49169', 
    '49170', '49171', '49172', '49173', '49174', '49175', '49176', '49177', '49178', 
    '49179', '49180', '49181', '49182', '49183', '49184', '49185', '49186', '49187', 
    '49188', '49189', '49190', '49191', '49192', '49193', '49194', '49195', '49196', 
    '49197', '49198', '49199', '49200'   # Dynamic/Private Ports (Ephemeral ports)
)

additional_ports = (
    '19',   # Chargen (Character Generator Protocol)
    '69',   # TFTP (Trivial File Transfer Protocol)
    '88',   # Kerberos
    '161',  # SNMP (Simple Network Management Protocol)
    '162',  # SNMP trap
    '389',  # LDAP (Lightweight Directory Access Protocol)
    '636',  # LDAPS (LDAP over SSL)
    '179',  # BGP (Border Gateway Protocol)
    '500',  # IKE (Internet Key Exchange) for VPNs
    '514',  # Syslog
    '546',  # DHCPv6 client
    '547',  # DHCPv6 server
    '993',  # IMAP over SSL (repetida da sua lista)
    '989',  # FTPS (Data)
    '990',  # FTPS (Control)
    '1194', # OpenVPN
    '1812', # RADIUS (Authentication)
    '1813', # RADIUS (Accounting)
    '3268', # Global Catalog (LDAP)
    '3306', # MySQL (repetida da sua lista)
    '3389', # RDP (Remote Desktop Protocol, repetida)
    '5061', # SIP-TLS (Session Initiation Protocol over TLS)
    '5432', # PostgreSQL
    '6379', # Redis
    '6667', # IRC (Internet Relay Chat)
    '8008', # HTTP Alternative
    '8086', # InfluxDB
    '9200', # Elasticsearch
    '11211', # Memcached
    '27017', # MongoDB
    '50000'  # SAP Router
)

def portscan():
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        client.settimeout(0.2)
        
        try:
            res = client.connect_ex((ip, int(port)))

            if res == 0:
                print(f'{port} OPEN')
                
        except:
            pass
        finally:
            client.close()

def main():
    portscan()

if __name__ == '__main__':
    main()
