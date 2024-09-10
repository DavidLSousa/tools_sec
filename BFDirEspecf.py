#!/usr/bin/env python3
import sys
import requests

url = sys.argv[1]

directories = (
    'portal','panel','members','user','profile','account','login','signup','register','forum','forums','blog','blogs','news','articles','media','gallery','galleries','video','videos','audio','audios','podcast','rss','feed','feeds','newsletter','mailing','contact','contacts','help','support','faq','terms','privacy','legal','about','about-us','careers','jobs','services','pricing','plans','products','store','shop','cart','checkout','order','orders','invoice','billing','payment','pay','subscribe','unsubscribe','feedback','reviews','comments','ratings','testimonials','portfolio','projects','clients','partners','events','event','calendar','meetup','conference','seminar','webinar','location','locations','branch','branches','map','sitemap','search','find','query','result','results','lookup','database','dbase','dbadmin','sql','mysql','restore','recovery','debug','trace','traceback','auth','oauth','session','sessions','token','tokens','hash','hashes','encrypt','encryption','decryption','cipher','ciphertext','privatekey','publickey','cert','certs','certificate','certificates','ssl','tls','key','keys','admin_panel','admin_login','user_login','user_register','staff','staff_login','staff_portal','reports','analytics','statistics','stats','tracking','track','monitor','monitoring','logfile','logfiles','archive','archives','repository','repositories','download','media_upload','media_download'
    )

directories_2 = (
    'portal/panel', 'portal/members', 'portal/login', 'portal/register',
    'portal/blog', 'portal/news', 'portal/articles', 'portal/media',
    'panel/user', 'panel/profile', 'panel/account', 'panel/login', 'panel/signup', 'panel/register',
    'members/profile', 'members/account', 'members/subscriptions',
    'user/login', 'user/register', 'user/profile', 'user/settings',
    'profile/account', 'profile/settings', 'profile/preferences',
    'account/billing', 'account/orders', 'account/invoices', 'account/subscriptions',
    'login/forgot-password', 'login/reset', 'login/oauth',
    'signup/confirm', 'signup/welcome',
    'forum/posts', 'forum/topics', 'forum/replies',
    'blog/posts', 'blog/comments', 'blog/authors',
    'media/gallery', 'media/upload', 'media/download', 'media/videos', 'media/images',
    'store/products', 'store/cart', 'store/checkout', 'store/orders',
    'order/invoice', 'order/tracking', 'order/confirmation',
    'payment/billing', 'payment/subscription', 'payment/invoice',
    'subscribe/newsletter', 'subscribe/podcast',
    'feedback/reviews', 'feedback/comments',
    'events/calendar', 'events/meetup', 'events/conference',
    'location/map', 'location/branches',
    'admin_panel/login', 'admin_panel/dashboard',
    'auth/session', 'auth/token',
    'reports/analytics', 'reports/statistics', 'reports/logs',
    'support/help', 'support/contact', 'support/faq',
    'privacy/terms', 'privacy/policy',
    'settings/account', 'settings/privacy',
    'database/sql', 'database/backup', 'database/recovery',
    'logs/error', 'logs/access', 'logs/archive'
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
    bruteForce(url, directories)
    bruteForce(url, directories_2)


if __name__ == '__main__':
    main()
