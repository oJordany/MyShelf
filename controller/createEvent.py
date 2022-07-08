from email import header
from urllib import response
import requests
import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication
import json
from controller.request import request
from confidential.confidential import *

client_secret = decrypt('confidential.txt', 1)[2] 
app_id = decrypt('confidential.txt', 1)[3] 
SCOPES = ["User.Read", "Calendars.Read.Shared", "Calendars.ReadWrite", "Calendars.Read", "Calendars.ReadWrite.Shared", "User.Export.All"]

authority_url = "https://login.microsoftonline.com/consumers/"
base_url = "https://graph.microsoft.com/v1.0/"

endpoint = base_url + 'me/events'

client_instance = ConfidentialClientApplication(
    client_id=app_id,
    client_credential=client_secret,
    authority=authority_url
)

# authorization_request_url = client_instance.get_authorization_request_url(SCOPES)
# print(authorization_request_url)
# webbrowser.open(authorization_request_url, new=True)

def refresh_token():
    # with open("confidential/confidential.json", "r") as confidential:
    #     confidential_object = json.load(confidential)
    confidential_object = json.loads(decrypt('confidential.json', 2)[0])
    access_token_refresh = client_instance.acquire_token_by_refresh_token(
        refresh_token=confidential_object["refresh_token"],
        scopes=SCOPES
    )
    access_token_refresh_json = json.dumps(access_token_refresh)
    with open("confidential/confidential.json", "w") as confidential:
        confidential.write(access_token_refresh_json)
    updated_encryption()
    return access_token_refresh["access_token"]

# authorizaton_code = "M.R3_BAY.4a3bdfc1-ead1-03d0-47d6-3695c65aa54f"
# access_token = client_instance.acquire_token_by_authorization_code(
#     code=authorizaton_code,
#     scopes=SCOPES
# )

access_token_id = refresh_token()


headers = {"Authorization": "Bearer "+access_token_id}

def construct_event_detail(event_name, **event_details):
    request_body = {
        'subject': event_name,
    }
    for key, val in event_details.items():
        request_body[key] = val
    return request_body

# event_name = 'Read Notification'
# body = {
#     'ContentType': 'HTML',
#     'Content': f'''<p>you have a book to read on your virtual bookshelf.</p><p>Don't waste time, start reading the book &quot;book&quot; right now.</p>'''
# }
# start = {
#     'DateTime': '2022-07-19T08:00:00',
#     'TimeZone': 'America/Sao_Paulo'
# }

# end = {
#     'DateTime': '2022-07-19T23:00:00',
#     'TimeZone': 'America/Sao_Paulo'
# }

# attendees = [
#     {
#         'EmailAddress': {
#             "Address":'jordanyluiz@outlook.com',
#         },
#         'Type': 'Required'
#     },
# ]

def create_event_detail(event_name, body, start, end, attendees):
    response1_create = requests.post(
        endpoint,
        headers=headers,
        json=construct_event_detail(
            event_name=event_name,
            body=body,
            start=start,
            end=end,
            attendees=attendees,
        )
    )
