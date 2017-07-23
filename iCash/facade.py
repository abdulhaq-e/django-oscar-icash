"""
Bridging module between Oscar and the gateway module (which is Oscar agnostic)
"""
from oscar.apps.payment import exceptions

from iCash import gateway

class Facade:
    """
    A bridge between oscar's objects and the core gateway object
    """

    def __init__(self, *args, **kwargs):
        gateway_url = kwargs.get('gateway_url')
        qr_gateway_url = kwargs.get('qr_gateway_url')
        self.gateway = gateway.GatewayConnector(gateway_url, qr_gateway_url)
            
    def login(self, params):
        self.gateway.login(params)

    def send_invoice(self, shop_card_no, customer_card_no, amount, confirmation_code):
        self.gateway.send_invoice(shop_card_no, customer_card_no,
                                  amount, confirmation_code)
        
    def confrimation_code_qr_image(self, shop_no, amount):
        return self.gateway.confrimation_code_qr_image(shop_no, amount)