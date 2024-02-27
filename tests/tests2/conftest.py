from dataclasses import dataclass
from typing import Any

import factory
import pytest
from faker import Faker
from pytest_factoryboy import named_model, register

import constants
from background import ReportCreated
from handlers.tags import TagBody
from models.reports import Report

from models.tags import TagModel
from services.tags import Tag
from services.tags import NonUniqueName


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
            constants.S_TAGS: mocker.MagicMock(),
            constants.S_RABBITMQ: mocker.MagicMock(),
            constants.S_REPORTS: mocker.MagicMock(),
        }
    )


@dataclass
class GenericAsyncFunc:
    return_value: Any

    async def __call__(self, *args,  **kwargs):
        return self.return_value

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_):
        return None


@pytest.fixture
def async_func():
    return GenericAsyncFunc


@pytest.fixture
def tag():
    return Tag(id=10, name="test_tag_name")


@pytest.fixture
def tag_mock(request, async_func, tag):
    if isinstance(request.param, Exception):
        return request.param
    if request.param is None:
        return async_func(return_value=request.param)
    return async_func(return_value=tag)


@register
class TagFactory(factory.Factory):
    class Meta:
        model = Tag

    id = factory.Faker("uuid4")
    name = "test_name"

# test background


class EventBaseBody(factory.Factory):
    report_id = factory.Faker("pyint")


@register
class EventBodyFactory(EventBaseBody):

    class Meta:
        model = named_model(dict, "EventBody")

    project_id = factory.Faker("pyint")
    test_id = 333
    session_id = factory.Faker("pyint")
    timestamp = factory.Faker("pyint")


@dataclass
class Application:
    srv_reports: str
    srv_tags: str
    srv_rabbitmq: str

    def __getitem__(self, item):
        return getattr(self, item)


@pytest.fixture
def mock_app(mocker):
    return Application(
        srv_reports=mocker.MagicMock(),
        srv_tags=mocker.MagicMock(),
        srv_rabbitmq=mocker.MagicMock(),
    )


@register
class ReportFactory(factory.Factory):
    class Meta:
        model = Report

    id = 111
    test_id = 333


@pytest.fixture
def report_mock(request):
    if request.param is None:
        return request.param
    return ReportFactory(test_id=request.param)
