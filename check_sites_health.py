import argparse
from socket import socket


def get_list_urls(path):
    list_urls = open(path, 'r', encoding='utf-8')
    list_urls = list_urls.read()
    return list_urls.split(',')


def load_urls4check(list_urls):
    for url in list_urls:
        s = socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(url,'43')



def is_server_respond_with_200(url):
    pass


def get_domain_expiration_date(domain_name):
    pass


if __name__ == '__main__':
    pass
