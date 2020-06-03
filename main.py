import os
import slack


API_KEY = os.environ["SLACK_API_KEY"]

# init web client
client = slack.WebClient(token=API_KEY)


response = client.users_conversations(types="public_channel,private_channel,mpim,im")
assert response["ok"]
