import pytest
from services.nomad import (
    Nomad,
    NomadResponse,
    NodeCapacity,
    DatacenterCapacity,
    DatacenterState,
)
from services.datacenters import HealthState
from asynctest import mock


@mock.patch.object(Nomad, "_is_server_healthy", return_value=True)
@pytest.mark.asyncio
async def test_check_datacenter_state_healthy_empty_nodes(mock_session, async_func):
    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    result = await manager.check_datacenter_state()
    assert isinstance(result, DatacenterState)
    assert result.health_state == HealthState.UNHEALTHY


@mock.patch.object(Nomad, "_is_server_healthy", return_value=False)
@pytest.mark.asyncio
async def test_check_datacenter_state_unhealthy(mock_session, async_func):
    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    result = await manager.check_datacenter_state()
    assert isinstance(result, DatacenterState)
    assert result.health_state == HealthState.UNHEALTHY
