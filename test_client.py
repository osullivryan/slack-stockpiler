from main import get_all_channels, get_conversations

import pytest
import os
import slack


@pytest.fixture
def mock_client():
    API_KEY = os.environ["SLACK_API_KEY"]
    return slack.WebClient(token=API_KEY)


@pytest.fixture
def mock_channel():
    return os.environ["SLACK_MOCK_CHANNEL"]


def test_get_all_channels(mock_client):
    channels = get_all_channels(mock_client)
    assert channels


def test_get_conversation_history(mock_client, mock_channel):
    conversation = get_conversations(mock_client, mock_channel)
    assert conversation
