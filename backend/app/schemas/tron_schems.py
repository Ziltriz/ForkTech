from pydantic import BaseModel, ConfigDict, field_validator
from decimal import Decimal

class TronAddressInfo(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance: int
    
    
    model_config = ConfigDict(from_attributes=True)

class AddressQueryCreate(TronAddressInfo):
    pass

class AddressQueryOut(AddressQueryCreate):
    id: int
    address: str
    bandwidth: int
    energy: int
    balance: Decimal  
    
    @field_validator('balance', mode='before')
    def convert_balance(cls, v):
        if isinstance(v, Decimal):
            return int(v)
        return v
    
    model_config = ConfigDict(from_attributes=True)

class PaginatedResponse(BaseModel):
    total: int
    page: int
    per_page: int
    items: list[AddressQueryOut]