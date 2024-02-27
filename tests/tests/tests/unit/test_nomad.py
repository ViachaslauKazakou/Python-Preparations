from unittest import mock

import aiohttp
import pytest

from services.datacenters import HealthState
from services.nomad import DatacenterState, Nomad


@pytest.mark.parametrize(
    "async_health, side_effect, health, async_nodes",
    [
        (True, None, "UNHEALTHY", []),
        (False, None, "UNHEALTHY", []),
        (False, aiohttp.ClientError, "UNREACHABLE", []),
        (True, None, "HEALTHY", [{"ID": 1}]),
    ],
    indirect=["async_health", "async_nodes"],
)
@pytest.mark.asyncio
async def test_check_datacenter_state(
    async_health,
    side_effect,
    health,
    async_nodes,
    mock_session,
    async_func,
    mocker,
    async_datacenters_capacity,
    async_reserved_resources,
):
    mocker.patch.object(
        Nomad,
        "_is_server_healthy",
        side_effect=mock.MagicMock(return_value=async_health, side_effect=side_effect),
    )
    mocker.patch.object(Nomad, "_get_nodes", side_effect=mock.MagicMock(return_value=async_nodes))
    mocker.patch.object(
        Nomad,
        "_get_datacenter_capacity",
        side_effect=mock.MagicMock(return_value=async_datacenters_capacity),
    )
    mocker.patch.object(
        Nomad,
        "_get_extra_reserved_resources",
        side_effect=mock.MagicMock(return_value=async_reserved_resources),
    )

    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    result = await manager.check_datacenter_state()

    assert isinstance(result, DatacenterState)
    assert result.health_state == getattr(HealthState, health)
