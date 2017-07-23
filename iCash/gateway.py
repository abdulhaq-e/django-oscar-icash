import json
import requests
import time

import urllib.parse

from django.utils.http import urlencode
from django.utils import six
from django.utils.six.moves.urllib.parse import parse_qsl

from iCash import exceptions


class GatewayConnector:
    
    def __init__(self, gateway_url, qr_gateway_url):
        self.gateway_url = gateway_url
        self.qr_gateway_url = qr_gateway_url
    
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
        url = urllib.parse.urljoin(self.gateway_url, 'token')
        self.login_response = requests.post(
            url, data=payload,
            headers={'content-type': 'application/json; charset=utf-8',
                     'Accept': 'application/json'})
        return self.login_response
    
    @property
    def token(self):
        return json.loads(self.login_response.content.decode('utf8')).get('access_token')

    def send_invoice(self, shop_card_no, customer_card_no, amount, confirmation_code):
        url_fragment = "api/sendInvoice/{}/{}/{}/{}".format(
            shop_card_no, customer_card_no, amount, confirmation_code)
        url = urllib.parse.urljoin(self.gateway_url, url_fragment)
        response = requests.get(url, headers={
            'Authorization': 'Bearer {}'.format(self.token)
        })
        print(url)
        print(response.content)
        if int(response.content.decode('utf8')) < 0:
            raise exceptions.iCashError

    def confrimation_code_qr_image(self, shop_no, amount):
        url_fragment = '/api/qrimage/{}/{}'.format(amount, shop_no)
        url = urllib.parse.urljoin(self.qr_gateway_url, url_fragment)
        
        return url
