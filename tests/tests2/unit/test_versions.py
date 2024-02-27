import pytest
from aiohttp import web

import constants
from __version__ import __version__
from src.handlers.versions import get


@pytest.mark.asyncio
async def test_get(mock_request):

    mock_request.app[constants.APP_NAME] = constants.APP_NAME
    mock_request.app[constants.APP_HOST] = constants.APP_HOST
    result = await get(mock_request)
    expected = web.json_response(
        {
            "name": constants.APP_NAME,
            "hostname": constants.APP_HOST,
            "version": __version__,
        }
    )
    assert result.status == 200
    assert result.text == expected.text
