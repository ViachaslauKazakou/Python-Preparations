import pytest
from unittest import mock
from services.datacenters_background import DatacentersBackground
from services.locations import Location, Locations, LocationType
import logging
from services.datacenters import Datacenter, Datacenters
from models.locations import LocationsDB, LocationModel


@pytest.mark.parametrize(
    "datacenter_type",
    [
        "azur",
        "aws",
    ],
)
@pytest.mark.asyncio
async def test_dcb_update_datacenters_ok(
        mocker,
        location_factory,
        async_locations,
        async_datacenters,
        datacenter_type
):
    mock_location = mocker.patch.object(Locations, "list", side_effect=mock.MagicMock(return_value=async_locations))

    mock_datacenter = mocker.patch.object(Datacenters, "get_by_location_id", side_effect=mock.MagicMock(return_value=async_datacenters))
    mock_location.type = "hjwegfye"
    logs = mocker.patch("logging.Logger")
    logs.return_value = mock.MagicMock()
    manager = DatacentersBackground(
        Locations(LocationsDB(location_factory)), Datacenters, logging.Logger, 30
    )
    result = await manager.update_datacenters()
    assert result == None
    mock_location.assert_called_once()
    mock_datacenter.assert_called_once()
