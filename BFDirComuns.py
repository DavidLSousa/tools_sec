#!/usr/bin/env python3
import sys
import requests

domain = sys.argv[1]

# Add Cookies na requisição, se necessário, assim, pode burlar um cloudfare
# Automação:
    # Buscar no navegador inf de USER_AGENT e COOKIES, e usar isso para fazer a requisição

# Pesquisar sobre o uso de threads no Burte Force

directories = (
    'index', 'images', 'downloads', 'admin', 'login', 'uploads', 'assets', 'css', 'js', 'api', 'includes', 'scripts', 'styles', 'img', 'files', 'backup', 'data', 'db', 'cgi-bin', 'logs', 'temp', 'private', 'docs', 'config', 'configurations', 'test', 'tests', 'bin', 'modules', 'resources', 'lib', 'web', 'static', 'public', 'home', 'dashboard', 'control', 'content', 'wp-admin', 'wp-content', 'wp-includes', 'phpmyadmin', 'secure', 'private_html', 'html', 'cgi', 'backup', 'user', 'mail', 'email', 'error', 'errors', 'favicon.ico', 'robots.txt', 'sitemap.xml'
    )

directories_2 = (
    'index/images', 'index/css', 'index/js', 'index/api', 'index/assets', 
    'index/uploads', 'index/data', 'index/db', 'index/logs', 'index/docs', 
    'index/config', 'index/public', 'index/home', 'index/admin', 'index/login', 
    'index/user', 'index/mail', 'index/error', 'index/favicon.ico', 'index/robots.txt', 
    'index/sitemap.xml',

    'login/uploads', 'login/css', 'login/js', 'login/api', 'login/assets', 
    'login/data', 'login/db', 'login/logs', 'login/docs', 'login/config',
    'login/public', 'login/home', 'login/admin', 'login/user', 'login/mail',
    'login/error', 'login/favicon.ico', 'login/robots.txt', 'login/sitemap.xml'
)


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
    url = f'http://{domain}'
    bruteForce(url, directories)
    bruteForce(url, directories_2)


if __name__ == '__main__':
    main()
