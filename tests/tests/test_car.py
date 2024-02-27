import pytest
from unittest import mock
from code.async_class import Car
import asyncio


@mock.patch.object(Car, "_check_key")
@pytest.mark.asyncio
async def test_car(mock_key):
    mock_key.side_effect = mock.MagicMock(return_value=True)
    manager = Car("Ford", False)
    result = await manager.start()
    assert result == "started"