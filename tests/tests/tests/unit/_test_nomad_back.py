import aiohttp
import pytest
from unittest import mock
# from conftest import mock_session

from services.datacenters import HealthState
from services.nomad import DatacenterCapacity, DatacenterState, NodeCapacity, Nomad, NomadResponse, Resource


@pytest.mark.parametrize(
    "async_health, side_effect, health, async_nodes",
    [
        (True, None, "UNHEALTHY", []),
        (False, None, "UNHEALTHY", []),
        (False, aiohttp.ClientError, "UNREACHABLE", []),
        (True, None, "UNHEALTHY", [{"ID": 1}]),
    ],
    indirect=["async_health", "async_nodes"]

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
    async_reserved_resources

):
    mocker.patch.object(Nomad, "_is_server_healthy", side_effect=mock.MagicMock(
        return_value=async_health, side_effect=side_effect)
                        )
    mocker.patch.object(Nomad, "_get_nodes", side_effect=mock.MagicMock(return_value=async_nodes))
    mocker.patch.object(Nomad, "_get_datacenter_capacity", side_effect=mock.MagicMock(
        return_value=async_datacenters_capacity)
                        )
    mocker.patch.object(Nomad, "_get_extra_reserved_resources", side_effect=mock.MagicMock(
        return_value=async_reserved_resources)
                        )

    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    result = await manager.check_datacenter_state()

    assert isinstance(result, DatacenterState)
    assert result.health_state == getattr(HealthState, health)

import aiohttp
import pytest

from services.datacenters import HealthState
from services.nomad import DatacenterState, Nomad, Resource


@mock.patch.object(Nomad, "_is_server_healthy", return_value=True)
@pytest.mark.asyncio
async def test_check_datacenter_state_healthy_empty_nodes(mock_session, async_func):
    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    result = await manager.check_datacenter_state()
    assert isinstance(result, DatacenterState)
    assert result.health_state == HealthState.UNHEALTHY


@mock.patch.object(Nomad, "_is_server_healthy", return_value=False)
@pytest.mark.asyncio
async def test_check_datacenter_state_unhealthy(mock_healthy, mock_session, async_func):
    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    result = await manager.check_datacenter_state()
    assert isinstance(result, DatacenterState)
    assert result.health_state == HealthState.UNHEALTHY


@mock.patch.object(Nomad, "_get_extra_reserved_resources")
@mock.patch.object(Nomad, "_get_datacenter_capacity")
@mock.patch.object(Nomad, "_get_nodes")
@mock.patch.object(Nomad, "_is_server_healthy", return_value=True)
@pytest.mark.asyncio
async def test_check_datacenter_state_unhealthy_with_node(
    mock_session,
    mock_nodes,
    mock_datacenter_capacity,
    mock_reserved_resources,
    async_func,
    datacenter_capacity_factory,
    resource_factory,
):
    mock_session.get.side_effect = mock.MagicMock(name="mocker_session", status=200)
    mock_datacenter_capacity.return_value = datacenter_capacity_factory()
    mock_nodes.return_value = [{"ID": 1}]
    mock_reserved_resources.return_value = resource_factory()
    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    result = await manager.check_datacenter_state()
    assert isinstance(result, DatacenterState)
    assert result.health_state == HealthState.UNHEALTHY


@mock.patch.object(Nomad, "_is_server_healthy", side_effect=aiohttp.ClientError)
@pytest.mark.asyncio
async def test_check_datacenter_state_healthy_except(mock_session, async_func):
    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    result = await manager.check_datacenter_state()
    assert isinstance(result, DatacenterState)
    assert result.health_state == HealthState.UNREACHABLE


@mock.patch.object(Nomad, "_get_extra_reserved_resources")
@mock.patch.object(Nomad, "_get_datacenter_capacity")
@mock.patch.object(Nomad, "_get_isas")
@mock.patch.object(Nomad, "_get_nodes_collection")
@mock.patch.object(Nomad, "_get_nodes")
@mock.patch.object(Nomad, "_is_server_healthy")
@pytest.mark.asyncio
async def test_check_datacenter_state_datacenter_capacity(
    mock_is_server_healthy,
    mock_nodes,
    mock_node_collection,
    mock_isas,
    mock_datacenter_capacity,
    mock_get_extra_reserved_resources,
    mock_session,
    async_func,
    single_node_factory,
    datacenter_capacity_factory,
):
    manager = Nomad(1, "host.com", 8000, "dt1", mock_session)
    mock_is_server_healthy.return_value = True
    mock_nodes.return_value = [{"ID": 1}]
    mock_node_collection.return_value = single_node_factory.create_batch(1)
    mock_datacenter_capacity.return_value = datacenter_capacity_factory()
    mock_isas.return_value = [{}, {}]
    mock_get_extra_reserved_resources.return_value = Resource(18, 1024)
    result = await manager.check_datacenter_state()
    assert isinstance(result, DatacenterState)
    assert result.health_state == HealthState.HEALTHY