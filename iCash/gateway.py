import json
import requests
import time

import urllib.parse

from django.utils.http import urlencode
from django.utils import six
from django.utils.six.moves.urllib.parse import parse_qsl

from iCash import exceptions


class GatewayConnector:

    def __init__(self, *args, **kwargs):
        self.merchant_gateway_url = kwargs.get('merchant_gateway_url')
        
    def url_builder(self, operation):
        base = 'api'
        if operation == 'send_invoice':
            fragment = base + '/sendInvoice'
        elif operation == 'can_pay':
            fragment = base + '/supported'
        elif operation == 'login':
            fragment = 'token'
            
        return urllib.parse.urljoin(self.merchant_gateway_url, fragment)

    def login(self, params):
        """
        Make a POST request to the URL to obtain a token to be used in communicating
        with the API.

        :params: must be a dict that includes the following:
        {
            'username': username
            'password': password
            'grant_type': 'password'
        }
        The data must be form encoded.
        """
        payload = params
        url = self.url_builder('login')
        self.login_response = requests.post(
            url, data=payload,
            headers={'content-type': 'application/json; charset=utf-8',
                     'Accept': 'application/json'})
        return self.login_response

    @property
    def token(self):
        return json.loads(self.login_response.content.decode('utf8')).get('access_token')

    def can_pay(self, params):
        '''
        params:
            - CustomerCard: int, required
            - ShopCard: int, optional
            - Amount: decimal number, required
            - Currency: int, optional
        '''
        url = self.url_builder('can_pay')
        print(url)
        payload = params
        auth_header = 'Bearer {}'.format(self.token)
        response = requests.post(url, json=payload, headers={
            'Authorization': auth_header})
        
        return response

    def send_invoice(self, params):
        '''
        params:
            - CustomerCard: int, required
            - ShopCard: int, optional
            - Amount: decimal number, required
            - Currency: int, optional
            - PayCode: int, required
            - ShopId: int, optional
        '''        
        url = self.url_builder('send_invoice')
        auth_header = 'Bearer {}'.format(self.token)
        response = requests.get(url, headers={
            'Authorization': auth_header})
        
        return response

    def paycode_qr_image(self, response):
        image = response.content.decode('utf8').get('qr_image')

        return image
