from argparse import ArgumentParser
import requests
import whois
import datetime

def parser_command_line():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', nargs='?', required=True,
                        dest='filepath')
    option = parser.parse_args()
    return option


def get_list_urls(path):
    list_urls = open(path, 'r', encoding='utf-8')
    list_urls = list_urls.read()
    return list_urls.split()


def get_response_whois(url):
    response_whois = whois.whois(url)
    return response_whois


def is_server_respond_with_200(url):
    request = requests.get(url)
    status_website = request.status_code
    if status_website == 200:
        return status_website


def get_domain_expiration_date(response_whois):
    expiration_date = response_whois.expiration_date
    return expiration_date


def get_result_of_the_check(url):
    pass


if __name__ == '__main__':
    option = parser_command_line()
    path = option.filepath
    list_urls = get_list_urls(path)
    for url in list_urls:
        response_whois = get_response_whois(url)
        print(get_domain_expiration_date(response_whois))
