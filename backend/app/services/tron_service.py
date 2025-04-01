from tronpy import Tron
from tronpy.providers import HTTPProvider
from app.core.config import settings
from app.schemas.tron_schems import TronAddressInfo



class TronService:
    def __init__(self):
        self.client = Tron(HTTPProvider(settings.TRON_NETWORK))

    async def get_address_info(self, address: str) -> TronAddressInfo:
        account = self.client.get_account(address)
        balance = self.client.get_account_balance(address)
        
        return TronAddressInfo(
            address=address,
            bandwidth=account.get("free_net_usage", 0),
            energy=account.get("energy", 0),
            balance=balance
        )