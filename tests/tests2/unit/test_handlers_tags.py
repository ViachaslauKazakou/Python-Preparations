import pytest
from aiohttp import web

import constants as consts
from services.tags import NonUniqueName
from src.handlers.tags import get_all, update, create, delete, tag_report, untag_report, tag_test, untag_test, TagBody
from services.tags import Tag


@pytest.mark.asyncio
async def test_get_all(mock_request, async_func, tag):
    mock_request.app[consts.S_TAGS].list.side_effect = async_func(return_value=[tag])
    expected = web.json_response({"tags": [tag.to_json() for tag in [tag]]})
    result = await get_all(mock_request)
    assert result.status == expected.status


@pytest.mark.asyncio
async def test_update_ok(mock_request, async_func, tag):
    mock_request.app[consts.S_TAGS].update.side_effect = async_func(return_value=tag)
    mock_request.app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
    expected = web.json_response({"tag": tag.to_json()})
    result = await update(mock_request, 1, TagBody(name="Tag_name"))
    assert result.status == expected.status


@pytest.mark.parametrize(
    "tag_mock, mock_exc",
    [
        (NonUniqueName(), web.HTTPConflict),
        (None, web.HTTPNotFound),
    ],
    indirect=["tag_mock"]
)
@pytest.mark.asyncio
async def test_update_exc(mock_request, async_func, tag_mock, mock_exc, tag):
    with pytest.raises(mock_exc):
        mock_request.app[consts.S_TAGS].update.side_effect = tag_mock
        mock_request.app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
        expected = web.json_response({"tag": tag.to_json()})
        result = await update(mock_request, 1, TagBody(name="Tag_name"))
        assert result.status == expected.status


@pytest.mark.asyncio
async def test_create_ok(mock_request, async_func, tag):
    mock_request.app[consts.S_TAGS].create.side_effect = async_func(return_value=tag)
    mock_request.app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
    expected = web.json_response({"tag": tag.to_json()}, status=201)
    result = await create(mock_request, TagBody(name="Tag_name"))
    assert result.status == expected.status
    mock_request.app[consts.S_TAGS].create.assert_called_once()
    mock_request.app[consts.S_RABBITMQ].send.assert_called_once()


@pytest.mark.asyncio
async def test_create_exc(mock_request, async_func):
    with pytest.raises(web.HTTPConflict):
        mock_request.app[consts.S_TAGS].create.side_effect = NonUniqueName
        await create(mock_request, TagBody(name="Tag_name"))
        mock_request.app[consts.S_TAGS].create.assert_called_once()


@pytest.mark.parametrize(
    "tag_mock",
    [
        None, "mock_tag"
    ],
    indirect=["tag_mock"]
)
@pytest.mark.asyncio
async def test_delete(mock_request, async_func, tag_mock, tag):
    mock_request.app[consts.S_TAGS].delete.side_effect = tag_mock
    mock_request.app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
    expected = web.json_response({"tag": tag.to_json()}, status=204)
    result = await delete(mock_request, 1)
    assert result.status == expected.status
    mock_request.app[consts.S_TAGS].delete.assert_called_once()


@pytest.mark.asyncio
async def test_tag_report_ok(mock_request, async_func, tag):
    mock_request.app[consts.S_TAGS].tag_report.side_effect = async_func(return_value=tag)
    mock_request.app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
    expected = web.json_response({"tag": tag.to_json()}, status=200)
    result = await tag_report(mock_request, 1, TagBody(name="Tag_name"))
    assert result.status == expected.status
    mock_request.app[consts.S_TAGS].tag_report.assert_called_once()
    mock_request.app[consts.S_RABBITMQ].send.assert_called_once()


@pytest.mark.asyncio
async def test_untag_report_ok(mock_request, async_func, tag):
    mock_request.app[consts.S_TAGS].untag_report.side_effect = async_func(return_value=tag)
    mock_request.app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
    expected = web.json_response({"tag": tag.to_json()}, status=204)
    result = await untag_report(mock_request, 1, TagBody(name="Tag_name"))
    assert result.status == expected.status
    mock_request.app[consts.S_TAGS].untag_report.assert_called_once()
    mock_request.app[consts.S_RABBITMQ].send.assert_called_once()


@pytest.mark.asyncio
async def test_tag_test_ok(mock_request, async_func, tag):
    mock_request.app[consts.S_TAGS].tag_test.side_effect = async_func(return_value=tag)
    mock_request.app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
    expected = web.json_response({"tag": tag.to_json()}, status=200)
    result = await tag_test(mock_request, 1, TagBody(name="Tag_name"))
    assert result.status == expected.status
    mock_request.app[consts.S_TAGS].tag_test.assert_called_once()
    mock_request.app[consts.S_RABBITMQ].send.assert_called_once()


@pytest.mark.asyncio
async def test_untag_test_ok(mock_request, async_func, tag):
    mock_request.app[consts.S_TAGS].untag_test.side_effect = async_func(return_value=tag)
    mock_request.app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
    expected = web.json_response({"tag": tag.to_json()}, status=204)
    result = await untag_test(mock_request, 1, 1)
    assert result.status == expected.status
    mock_request.app[consts.S_TAGS].untag_test.assert_called_once()
    mock_request.app[consts.S_RABBITMQ].send.assert_called_once()
