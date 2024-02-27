import pytest

import constants as consts
from src.background import report_created


@pytest.mark.asyncio
async def test_report_created(mocker, mock_app, event_body, async_func, report, tag):
    mock_app[consts.S_REPORTS].get_one.side_effect = async_func(return_value=report)
    mock_app[consts.S_TAGS].list_by_session_test.side_effect = async_func(return_value=[tag])
    mock_app[consts.S_RABBITMQ].send.side_effect = async_func(return_value=None)
    mocker.patch('asyncio.gather', new=async_func(return_value=None))
    await report_created(event_body, mock_app)
    mock_app[consts.S_REPORTS].get_one.assert_called_once()
    mock_app[consts.S_TAGS].list_by_session_test.assert_called_once()
    mock_app[consts.S_RABBITMQ].send.assert_called_once()


@pytest.mark.parametrize(
    "report_mock",
    [
        None, 555
    ],
    indirect=["report_mock"]
)
@pytest.mark.asyncio
async def test_report_created_error(mocker, mock_app, event_body, async_func, tag, report_mock):
    with pytest.raises(Exception):
        mock_report = mock_app[consts.S_REPORTS].get_one.side_effect = async_func(return_value=report_mock)
        await report_created(event_body, mock_app)
        mock_report.assert_called_once()

