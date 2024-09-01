#!/usr/bin/env python3
import sys
import requests

url = sys.argv[1]

# Add Cookies na requisição, se necessário, assim, pode burlar um cloudfare
# Automação:
    # Buscar no navegador inf de USER_AGENT e COOKIES, e usar isso para fazer a requisição

# Pesquisar sobre o uso de threads no Burte Force

def bruteForce(url, directories):
    for dir in directories:
        try:
            urlAlvo = f'{url}/{dir}'
            res = requests.get(urlAlvo, timeout=7)

            if res.status_code == 200:
                print(f'Diretório encontrado: {urlAlvo}')
            elif 300 <= res.status_code < 400:
                print(f'Redirecionado: {urlAlvo}')
            else:
                pass
            
        except:
            pass


def main():
    with open('/home/davidlsousa/lists/dir_comuns.txt') as directories:
        print(url)
        bruteForce(url, directories.read().splitlines())


if __name__ == '__main__':
    main()
