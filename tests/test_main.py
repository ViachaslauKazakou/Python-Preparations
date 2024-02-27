import pytest
from unittest import mock

import code.data_class
from code.data_class import Request


@mock.patch.object(code.data_class.Request, 'get')
def test_main(mock_get):
    mock_get.return_value = 'Done'
    manager = Request("data")
    result = manager.get()
    assert result == 'Done'
    mock_get.assert_called_once()