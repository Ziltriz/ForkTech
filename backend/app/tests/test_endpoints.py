import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.tron_schems import AddressQueryOut, PaginatedResponse
from unittest.mock import AsyncMock, patch
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
    
    print(response.json())
    assert response.status_code == 200
    assert response.json()["address"] == test_address

@pytest.mark.asyncio
@patch("app.services.database_service.DatabaseService")
async def test_get_queries(mock_db_service):
    test_data = [
        {
            "id": 1,
            "address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
            "bandwidth": 1000,
            "energy": 500,
            "balance": 1000000,
            "created_at": "2023-01-01T00:00:00"
        }
    ]
    
    mock_db_service.return_value.get_queries.return_value = (1, test_data)
    
    response = client.get("/queries/?page=1&per_page=10")
    
    assert response.status_code == 200
    assert response.json()["total"] == 1
    assert len(response.json()["items"]) == 1