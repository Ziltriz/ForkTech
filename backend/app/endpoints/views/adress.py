from fastapi import APIRouter, Depends, HTTPException
from app.schemas.tron_schems import AddressQueryOut
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.tron_service import TronService
from app.services.database_service import DatabaseService
from app.db.session import get_db

router = APIRouter(prefix=['/address'], tags=['adress'])

@router.post("/info", response_model=AddressQueryOut)
async def get_address_info(
    address: str,
    db: AsyncSession = Depends(get_db)
):
    tron_service = TronService()
    db_service = DatabaseService(db)
    
    try:
        address_info = await tron_service.get_address_info(address)
        query = await db_service.create_address_query(address_info)
        return query
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))