#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status '''
from urllib import request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as resp:
        result = resp.read()
        print('Body response:')
        print('\t- type: {}'.format(type(result)))
        print('\t- content: {}'.format(result))
        print('\t- utf8 content: {}'.format(result.decode('utf-8')))
