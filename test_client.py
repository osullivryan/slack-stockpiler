from main import get_all_channels

import pytest
import os
import slack


@pytest.fixture
def mock_client():
    API_KEY = os.environ["SLACK_API_KEY"]
    return slack.WebClient(token=API_KEY)


def test_get_all_channels(mock_client):
    channels = get_all_channels(mock_client)
    assert channels
