import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.tron_schems import AddressQueryOut
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.database_service import DatabaseService
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime

client = TestClient(app)

@pytest.mark.asyncio
@patch("app.services.tron_service.TronService")
@patch("app.services.database_service.DatabaseService")
async def test_get_address_info(mock_db_service, mock_tron_service):
    test_address = "TG81gtb1Fj32BwghvAqfYvLgnfXYuhdtHq"
    
    mock_tron_service.return_value.get_address_info.return_value = {
        "address": test_address,
        "bandwidth": 1000,
        "energy": 500,
        "balance": 1000000
    }
    
    mock_db_service.return_value.create_address_query.return_value = AddressQueryOut(
        id=1,
        address=test_address,
        bandwidth=1000,
        energy=500,
        balance=1000000,
        created_at=datetime.now()
    )
    
    response = client.post(
        f"/address/info/?address={test_address}",
    )
    

    assert response.status_code == 200
    assert response.json()["address"] == test_address

@pytest.mark.asyncio
async def test_get_queries():
    mock_session = AsyncMock(spec=AsyncSession)

    test_query = MagicMock()
    test_query.address = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
    test_data = [test_query]

    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = test_data

    mock_count_result = MagicMock()
    mock_count_result.scalar_one.return_value = 1

    async def execute_side_effect(query):
        if "count" in str(query):
            return mock_count_result
        return mock_result

    mock_session.execute.side_effect = execute_side_effect

    db_service = DatabaseService(mock_session)

    total_count, items = await db_service.get_queries(page=1, per_page=10)

    assert total_count == 1
    assert len(items) == 1
    assert items[0].address == test_query.address

    assert mock_session.execute.call_count == 2
    assert mock_result.scalars.call_count == 2
    assert mock_result.scalars.return_value.all.call_count == 2