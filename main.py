from slack.web.slack_response import SlackResponse
from slack.errors import SlackClientError
from slack import WebClient
from typing import Text, List


def check_response(response: SlackResponse) -> None:
    if not response["ok"]:
        assert SlackClientError("Could not get a response from the API")


def get_conversations(client: WebClient, channel: Text) -> dict:
    response = client.conversations_history(channel=channel)
    check_response(response)
    return response['messages']


def get_all_channels(client: WebClient) -> List[Text]:
    response = client.users_conversations(
        types="public_channel,private_channel,mpim,im"
    )
    check_response(response)
    return [channel["id"] for channel in response["channels"]]
