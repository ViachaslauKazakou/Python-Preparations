import pytest
from src.handlers.versions import get
import constants
from aiohttp import web
from __version__ import __version__


@pytest.mark.asyncio
async def test_get(mock_request):

    mock_request.app[constants.APP_NAME] = constants.APP_NAME
    mock_request.app[constants.APP_HOST] = constants.APP_HOST
    result = await get(mock_request)
    expected = web.json_response({"name": constants.APP_NAME, "hostname": constants.APP_HOST, "version": __version__})
    assert result.status == 200
    assert result.text == expected.text
