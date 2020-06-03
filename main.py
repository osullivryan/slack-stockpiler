from slack.web.slack_response import SlackResponse
from slack.errors import SlackClientError
from slack import WebClient


def check_response(response: SlackResponse) -> None:
    if not response["ok"]:
        assert SlackClientError("Could not get a response from the API")


def get_all_channels(client: WebClient) -> dict:
    response = client.users_conversations(
        types="public_channel,private_channel,mpim,im"
    )
    check_response(response)
    return response["channels"]
