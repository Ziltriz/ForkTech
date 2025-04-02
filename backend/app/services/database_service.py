from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import AddressQuery
from app.schemas.tron_schems import TronAddressInfo
from sqlalchemy.future import select
from sqlalchemy import desc


class DatabaseService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_address_query(self, data: TronAddressInfo) -> AddressQuery:
        query = AddressQuery(
            address=data.address,
            bandwidth=data.bandwidth,
            energy=data.energy,
            balance=data.balance
        )
        self.session.add(query)
        await self.session.commit()
        await self.session.refresh(query)
        return query
    
    async def get_queries(self, page: int = 1, per_page: int = 10) -> tuple[int, list[AddressQuery]]:
        offset = (page - 1) * per_page
        
        total_query = select(AddressQuery)
        result = await self.session.execute(total_query)
        total_count = len(result.scalars().all())
        
        queries = select(AddressQuery).order_by(desc(AddressQuery.created_at)).offset(offset).limit(per_page)
        result = await self.session.execute(queries)
        items = result.scalars().all()
        
        return total_count, items
    