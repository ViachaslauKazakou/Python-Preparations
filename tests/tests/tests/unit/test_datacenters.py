import pytest
from unittest import mock
from src.handlers.datacenters import get_all
from aiohttp import web
import constants as consts
from tests.conftest import DatacenterFactory
import json


def create_fake_datacenters(datacenter, expected_datacenter, datacenter_factory):
    if datacenter and expected_datacenter:
        datacenters_factory = datacenter_factory.create_batch(1)
        expected_datacenters = datacenters_factory
    elif datacenter and not expected_datacenter:
        datacenters = datacenter_factory()
        datacenters_factory = datacenters
        expected_datacenters = [datacenters]
    else:
        datacenters_factory = None
        expected_datacenters = []
    return datacenters_factory, expected_datacenters

@pytest.mark.parametrize(
    "location_id, datacenter, expected_datacenter",
    [
        (None, True, True),
        (1, True, False),
        (2, False, False)
    ]
)
@pytest.mark.asyncio
async def test_get_all(mock_request, location_id, datacenter, expected_datacenter,  async_func, datacenter_factory):

    datacenters_factory = create_fake_datacenters(datacenter, expected_datacenter, datacenter_factory)

    mock_request.app[consts.S_DATACENTERS].list.side_effect = async_func(return_value=datacenters_factory[0])
    mock_request.app[consts.S_DATACENTERS].get_by_location_id.side_effect = async_func(
        return_value=datacenters_factory[0]
    )

    expected = web.json_response({"datacenters": [datacenter.to_json() for datacenter in datacenters_factory[1]]})
    result = await get_all(mock_request, location_id=location_id)

    assert result.status == expected.status
    assert result.body == expected.body
    mock_request.app[consts.S_DATACENTERS].list.assert_called_once()