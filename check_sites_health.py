from argparse import ArgumentParser
import requests
import whois
from datetime import datetime, timedelta

def parser_command_line():
    parser = ArgumentParser()
    parser.add_argument('path', help='The path to the directory'
                        ' for finding file with the list websites', type=str)
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
    code_200_ok = 200
    request = requests.get(url)
    status_website = request.status_code
    if status_website == code_200_ok:
        return status_website


def get_domain_expiration_date(response_whois):
    expiration_date = response_whois.expiration_date
    type(expiration_date)
    if type(expiration_date) is list:
        expiration_date = expiration_date[0]
    return expiration_date


def get_subscription_period(expiration_date):
    of_days_in_the_month = timedelta(days=30)
    remaining_subscription = expiration_date - datetime.today()
    full_months = remaining_subscription // of_days_in_the_month
    return full_months


if __name__ == '__main__':
    option = parser_command_line()
    path = option.path
    critical_period = 1
    list_urls = get_list_urls(path)
    for url in list_urls:
        response_whois = get_response_whois(url)
        expiration_date = get_domain_expiration_date(response_whois)
        full_months = get_subscription_period(expiration_date)
        print('Website: ', url)
        print('Status: ', is_server_respond_with_200(url))
        if full_months > critical_period:
            print('Until the date of expiry of: {} months'.format(full_months))
            print('=' * 50)
        else:
            print('Attention! Subscription expires!')
            print('=' * 50)