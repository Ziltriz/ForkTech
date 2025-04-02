from tronpy import Tron
from tronpy.providers import HTTPProvider
from decimal import Decimal
from app.schemas.tron_schems import TronAddressInfo
from app.core.config import settings



class TronService:
    def __init__(self):
        self.client = Tron(
            HTTPProvider(
                endpoint_uri=settings.TRON_URI,
                api_key=settings.TRON_API_KEY
            )
        )

    async def get_address_info(self, address: str) -> TronAddressInfo:
        account = self.client.get_account(address)
        balance = self.client.get_account_balance(address)
        
        return TronAddressInfo(
            address=address,
            bandwidth=account.get("free_net_usage", 0),
            energy=account.get("energy", 0),
            balance=int(balance)
        )