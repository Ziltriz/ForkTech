from sqlalchemy import Column, String, Integer, BigInteger, DateTime
from sqlalchemy.sql import func
from app.db import Base

class AddressQuery(Base):
    __tablename__ = "address_queries"
    
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(42), index=True)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    balance = Column(BigInteger)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<AddressQuery {self.address}>"