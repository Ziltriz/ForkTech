from datetime import datetime
from pydantic import BaseModel

class TronAddressInfo(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance: int
    
    class Config:
        orm_mode = True

class AddressQueryCreate(TronAddressInfo):
    pass

class AddressQueryOut(AddressQueryCreate):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class PaginatedResponse(BaseModel):
    total: int
    page: int
    per_page: int
    items: list[AddressQueryOut]