import pytest
from unittest import mock
from src.handlers.versions import get
import aiohttp


@mock.patch.object(aiohttp.web, "json_response")
@pytest.mark.asyncio
async def test_get(mock_web):
    mock_web.return_value = {"datacenters": []}
    request = mock.AsyncMock()
    result = await get(request)
    assert result["datacenters"] == []
    mock_web.assert_called_once()