from argparse import ArgumentParser
import socket

def parser_command_line():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', nargs='?', required=True,
                        dest='filepath')
    option = parser.parse_args()
    return option


def get_list_urls(path):
    list_urls = open(path, 'r', encoding='utf-8')
    list_urls = list_urls.read()
    print(list_urls.split(','))
    return list_urls.split(',')


def load_urls4check(list_urls):
    url_who_is = 'whois.iana.org'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = sock.connect((url_who_is, 43))
    for url in list_urls:
        print(url + '\r\n')
        sock.send((url + '\r\n').encode())
        continue
        data_who_is = sock.recv()
    print(data_who_is.decode())


def is_server_respond_with_200(url):
    pass


def get_domain_expiration_date(domain_name):
    pass


if __name__ == '__main__':
    option = parser_command_line()
    path = option.filepath
    list_urls = get_list_urls(path)
    load_urls4check(list_urls)
