from dataclasses import dataclass
from typing import Any

import factory
import pytest
from aiohttp import ClientSession
from faker import Faker
from pytest_factoryboy import register

import constants
from models.locations import LocationModel
from services.datacenters import Datacenter, HealthState
from services.nomad import DatacenterCapacity, Resource, SingleNode


@dataclass
class GenericAsyncFunc:
    return_value: Any

    async def __call__(self, *args, **kwargs):
        return self.return_value

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_):
        return None


@dataclass
class Request:
    app: dict

    def __getitem__(self, item):
        return getattr(self, item)


@pytest.fixture
def mock_request(mocker):
    return Request(
        app={
            constants.APP_NAME: mocker.MagicMock(),
            constants.APP_HOST: mocker.MagicMock(),
            constants.S_DATACENTERS: mocker.MagicMock(),
        }
    )


@pytest.fixture
def async_func():
    return GenericAsyncFunc


fake = Faker()


@register
class DatacenterFactory(factory.Factory):
    class Meta:
        model = Datacenter

    id = factory.Faker("uuid4")
    location_id = factory.Faker("pyint")
    total_cpu_mhz = factory.Faker("random_int", min=1000, max=5000)
    total_cpu_cores = factory.Faker("random_int", min=4, max=32)
    total_clients = factory.Faker("random_int", min=10, max=100)
    total_memory_mb = factory.Faker("random_int", min=8192, max=32768)
    health_state = factory.Faker(
        "random_element",
        elements=[HealthState.HEALTHY, HealthState.UNHEALTHY, HealthState.UNREACHABLE],
    )
    updated_at = factory.Faker("unix_time")
    nodes = factory.Faker("pylist", nb_elements=5, variable_nb_elements=True)
    isas = factory.Faker("pylist", nb_elements=3, variable_nb_elements=True)


# Nomad fixtures


@pytest.fixture
async def mock_session():
    async with ClientSession() as session:
        yield session


@pytest.fixture
def fake_datacenters(request, datacenter_factory):
    datacenter = request.param

    if datacenter == 1:
        return [datacenter_factory.create_batch(1)] * 2
    elif datacenter > 2:
        datacenters_factory = datacenter_factory()
        return [datacenters_factory, [datacenters_factory]]

    return None, []


@register
class DatacenterCapacityFactory(factory.Factory):
    class Meta:
        model = DatacenterCapacity

    total_cpu: int = 5
    total_memory: int = 1024
    total_cores: int = 5
    total_clients: int = factory.Faker("pyint")
    nodes: int = factory.Faker("pyint")


@register
class ResourceFactory(factory.Factory):
    class Meta:
        model = Resource

    cpu: int = 2
    memory: int = 512


@register
class SingleNodeFactory(factory.Factory):
    class Meta:
        model = SingleNode

    id = factory.Faker("uuid4")
    data = {"NodeResources": None, "ReservedResources": None}


@pytest.fixture
async def async_health(request):
    return request.param


@pytest.fixture
async def async_nodes(request):
    return request.param


@pytest.fixture
async def async_datacenters_capacity(request):
    return DatacenterCapacityFactory()


@pytest.fixture
async def async_reserved_resources(request):
    return ResourceFactory()


# datacenter_background

@register
class LocationFactory(factory.Factory):
    class Meta:
        model = LocationModel

    id: int = factory.Faker("uuid4")
    type: str = "aws"
    orchestrator_host: str = factory.Faker("pystr")
    orchestrator_port: int = factory.Faker("pyint")
    orchestrator_datacenter: str = factory.Faker("pystr")


@pytest.fixture
async def async_locations(request):
    result = LocationFactory()
    result.type = "uehue"
    return [result]

@pytest.fixture
async def async_datacenters(request):
    return DatacenterFactory()
