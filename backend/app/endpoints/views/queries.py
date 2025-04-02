from fastapi import APIRouter, Depends
from app.schemas.tron_schems import PaginatedResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.database_service import DatabaseService
from app.db.session import get_db

router = APIRouter(prefix='/queries', tags=['queries'])

@router.get('', response_model=PaginatedResponse)
async def get_queries(
    page: int = 1,
    per_page: int = 10,
    db: AsyncSession = Depends(get_db)
):
    db_service = DatabaseService(db)
    total_count, items = await db_service.get_queries(
        page=page,
        per_page=per_page
    )

    return PaginatedResponse(
        total=total_count,
        page=page,
        per_page=per_page,
        items=items
    )