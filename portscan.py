#!/usr/bin/env python3
import sys
import socket

ip = sys.argv[1]

def portscan():
    with open('/home/davidlsousa/lists/ports.txt', 'r') as filePorts:
        ports = filePorts.read().splitlines()

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
