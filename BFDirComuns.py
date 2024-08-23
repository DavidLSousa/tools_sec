#!/usr/bin/env python3
import sys
import requests

url = sys.argv[1]


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
            
        except ValueError:
            print(ValueError)


def main():
    with open('/home/davidlsousa/lists/dir_comuns.txt') as directories:
        print(url)
        bruteForce(url, directories.read().splitlines())


if __name__ == '__main__':
    main()
