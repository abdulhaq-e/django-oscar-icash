"""
Bridging module between Oscar and the gateway module (which is Oscar agnostic)
"""
from django.conf import settings

from .exceptions import iCashError

from iCash import gateway

class Facade:
    """
    A bridge between oscar's objects and the core gateway object
    """

    def __init__(self, *args, **kwargs):
        self.gateway = gateway.GatewayConnector(
            merchant_gateway_url=settings.ICASH_MERCHANT_GATEWAY_URL)
            
    def login(self, params):
        self.gateway.login(params)

    @staticmethod
    def check_required_payload(params, required_params):
        for p in required_params:
            if not params.get(p, None):
                raise iCashError
        
    def can_pay(self, params):
        required_params = ['CustomerCard']
        self.check_required_payload(params, required_params)
        
        return self.gateway.can_pay(params)
        
    def send_invoice(self, params):
        required_params = ['CustomerCard', 'Amount', 'PayCode']
        self.check_required_payload(params, required_params)
                                
        response = self.gateway.send_invoice(params)
        if int(response.content.decode('utf8')) < 0:
            raise exceptions.iCashError
            
        return response
                
    def paycode_qr_image(self, response):
        return self.gateway.paycode_qr_image(response)