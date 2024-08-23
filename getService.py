#!/usr/bin/env python3
import sys
import socket

ip = sys.argv[1]
port = int(sys.argv[2])

# NAO ESTA FUNCIONANDO A PARTE DE SERVIÇO

def getService():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.settimeout(20)

    try:
        res = client.connect_ex((ip, port))

        if res == 0:
            servico = client.recv(1024).decode('utf-8')
            print(f'{port} OPEN')
            print(f'SERVIÇO: {servico}')
        else:
            print(f'{port} CLOSE')
            
    except ValueError:
        print(ValueError)
    finally:
        client.close()

def main():
    getService()

if __name__ == '__main__':
    main()
