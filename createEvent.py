from email import header
from urllib import response
import requests
import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication
import json
from controller.request import request

client_secret = "APt8Q~42eah3OYAKwX9qFfhjiQuVP~C09OCKva1W"
app_id = "78f82552-1b78-4ccb-8416-11e79a7170ee"
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

# authorizaton_code = "M.R3_BAY.663abfdc-a9e1-8823-148a-cd62044dc7eb"
# access_token = client_instance.acquire_token_by_authorization_code(
#     code=authorizaton_code,
#     scopes=SCOPES
# )

# print(access_token)
access_token_id = "EwCAA8l6BAAUkj1NuJYtTVha+Mogk+HEiPbQo04AAesLl7nKy7mD3aXmwOP5oykMSQeW5GqpxUYbRwchRvRtE+YObch+Oq5I1lYEo55wsm+PH3t08IU3rnLLRuOnegKa2vGxdGEO9XWBEdFjELc+iLVUEq7ka1hVZIEfLJrBWIsmSF5MaeB1uv8FR0ECMbkTWMVsy5bvrcsrfYTmV2MwmCiAM2BTN9is8nHtzSOqoy7wKjpLHYrA0CX/54nKCmAlxMg8WfMvnxrm8ACQE1kroH6VUXkLnLgmrqs0HC0pbklD5I79lrMw1/V0+6ecCMOAJ4iLlsSpmezz5Se04p4Zk4WsvIOP3aZPuGBzMme2RJ9P8uFIbL97d3AyUWgILwYDZgAACAv/X8VsepYYUAI1r3a5eV3DIzdR9NYHPqTUPoCHQVkjRXTHefqQHw0qLaS+zGRfZfqPVMixhteTSaiwwKiVPgO61nb8gGFw4E/ug5pnU6bwIrPrGAZkztgVGNoo3pnCNAUwIOCKxd3Fd6m5Zlv6AjwDlO1GSzLQ3zdqZQCL5eab0zNQS/dAIrXvY5TYUJaMzoRGzR/jHAZUVNzc26+mGGhgqX6WCkUIembY7Us8tUNWFM8vbAeEpgUTvW9yHzL3/VjV0PjLwpEOWYXIqrAmqD1OnMmjzqQarBZkYNFbNFofVFA+xpa3j13xbaXW4UjTcj+4B5d5MR1Xlr3UGBPaGQZMYpZGbzqSKmc7bSLivtHWnUAhlBmGMNP1XMYK8rfb8zU15BlG9eckbwvq5+S2yb7jjZQJzOKgWh+KcTGQNdCR6ZjLsI/6FPXP9bAXRbCKYZvtsYwI3mdrHVo4BspoBr5gwNv0bobi5gahbr707LHqAilxYrmpiWNg6Y9fG/H8H342Ck/KSGyA8kt1mpVI4Dq3D9VaNmhCJ/VZpIcVm9h6pnewy9MgRN0HMsQrutX+SZPZBtghHTcTTE6YnK1g6B6XZHhiZfQHgpi8QSMNZJhnMLRtz5Sm4wlbMzyE4o2+B2R9u/3tb9tZc9D1EdWDnodubJebggykReIwff3T6N82v8fKDDog7EAvaMJUEUznUm0tBJ6efU0tTCw7+41FdpGagUw929Ph0QM4j4iOjeX/2/oZCgqEzw7yYdhEUvwbpena7NbKy5TNwnZ2E8CLeARPyvywB0J3CnmHnwI="


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

    print(response1_create.json())