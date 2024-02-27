import pytest
from unittest import mock
from src.handlers.datacenters import get_all
import aiohttp


async def mock_list():
    return [mock.MagicMock(to_json=mock.MagicMock(return_value="datacenter"))]


async def mock_location():
    return mock.MagicMock(to_json=mock.MagicMock(return_value="datacenter"))

class Request:
    # Implement methods and attributes you need for testing
    app = {
        "srv_datacenters": mock.AsyncMock(
            list=mock.MagicMock(return_value=mock_list()),
            get_by_location_id=mock.MagicMock(return_value=mock_location())
        ),
    }


async def mock_request():
    return Request()

#
# @mock.patch.object(aiohttp.web, "json_response")
# @pytest.mark.asyncio
# async def test_get_all(mock_web):
#     mock_web.return_value = {"datacenters": []}
#     request = await mock_request()
#     result = await get_all(request)
#     assert result["datacenters"] == []
#     mock_web.assert_called_once()
#
#
# # @mock.patch.object(aiohttp.web, "Request")
# # @mock.patch.object(aiohttp.web.Request, "app")
# @mock.patch.object(aiohttp.web, "json_response")
# @pytest.mark.asyncio
# async def test_get_all_with_locations(mock_web):
#     mock_web.return_value = {"datacenters": []}
#     # mock_request.return_value = mock.AsyncMock(list=mock.AsyncMock(return_value="1"))
#     # mock_app.return_value = mock.AsyncMock()
#     request = await mock_request()
#     result = await get_all(request, location_id=1)
#     assert result["datacenters"] == []
#     mock_web.assert_called_once()


params = [
    (
        None,
        [],
        {"datacenters": []},
    ),
    (
        1,
        [],
        {"datacenters": []},
    ),
]


@mock.patch.object(aiohttp.web, "json_response")
@pytest.mark.parametrize("location_id, expected, result", params)
@pytest.mark.asyncio
async def test_getall(mock_web, location_id, expected, result):
    mock_web.return_value = result
    request = await mock_request()
    result = await get_all(request, location_id=location_id)
    assert result["datacenters"] == expected
    mock_web.assert_called_once()
