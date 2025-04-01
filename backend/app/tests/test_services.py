import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from app.services.tron_service import TronService
from app.services.database_service import DatabaseService
from app.schemas.tron_schems import TronAddressInfo
from app.db.models import AddressQuery

@pytest.mark.asyncio
async def test_create_address_query():
    mock_session = AsyncMock()
    db_service = DatabaseService(mock_session)
    
    test_data = TronAddressInfo(
        address="TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
        bandwidth=1000,
        energy=500,
        balance=1000000
    )
    
    result = await db_service.create_address_query(test_data)
    
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()
    assert isinstance(result, AddressQuery)

@pytest.mark.asyncio
@patch("tronpy.Tron.get_account")
@patch("tronpy.Tron.get_account_balance")
async def test_get_address_info(mock_balance, mock_account):
    mock_account.return_value = {"free_net_usage": 1000, "energy": 500}
    mock_balance.return_value = 1000000
    
    tron_service = TronService()
    result = await tron_service.get_address_info("TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t")
    
    assert result.address == "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
    assert result.bandwidth == 1000
    assert result.energy == 500
    assert result.balance == 1000000