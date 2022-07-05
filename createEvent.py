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
def refresh_token():
    with open("confidential/confidential.json", "r") as confidential:
        confidential_object = json.load(confidential)
    access_token_refresh = client_instance.acquire_token_by_refresh_token(
        refresh_token=confidential_object["refresh_token"],
        scopes=SCOPES
    )
    access_token_refresh_json = json.dumps(access_token_refresh)
    with open("confidential/confidential.json", "w") as confidential:
        confidential.write(access_token_refresh_json)
    return access_token_refresh["access_token"]
# authorizaton_code = "M.R3_BAY.4a3bdfc1-ead1-03d0-47d6-3695c65aa54f"
# access_token = client_instance.acquire_token_by_authorization_code(
#     code=authorizaton_code,
#     scopes=SCOPES
# )
access_token_id = refresh_token()
# access_token_id = "EwCAA8l6BAAUkj1NuJYtTVha+Mogk+HEiPbQo04AAakwCFfDqorAZCQBnDpztgMblTUJgX/FwD+YpX7DMAuY5SJVxdbXQJDLW2EeICUGz37TVNdRPxRU+uyXFaSuRaT9Qid87gjQjDNzaz/h6YJvhsMOWyXMDlUJ5drCkcpx1/SAkqDL01f6C5HBs6tB2DEqIIZW+F3etwLKFPrIlfSlnopCLByNb0oxKSbWOnzvCPtSmxhJbHmS2czTYFI4cbOzGJl2IElaPKDSf/0NJRqf059jbx8HO4qDlC0W+GnKqotZ3aKBziqZK8/2rGchSdwSFX1EOo5GbSlVFPMMD23Tvw3gVEX+wOi0V0LUgnBvKIjbOPtQcpoSYPF75N4MkUoDZgAACDmyWpzFEl2aUAKhqUyfx6DReUeZbUKLpgYXRM4Epe8ijbkQdKBrJ/ReqsOnsDAkKv8A8+ukc3beT+3ezXw5JKvfU0IIU+TyXUzO/zEbDVH5oI6MD003YtudrfLEAiVgNuD13UFw2HYV3FGkRk+serJnN4YmhtlkLSFsxAt/qJNxOd3+ED9afQH9RZPCDFuBu1WmKw668eIQBRbZu8Y7wxG99U2qhX73CIo9WiayCXWUuo0qL/BZXkxNn/6oVJAQUjLo8IaqW7THKbAyOCz4dyw2Ocxwt/thbjClPeM5feF133xGB+A+nDEhSYzBowsJEH5Q5ov0XxVfO8g8lTniIAAgYJD/BcpL6DIe9yg4hh5NIYHjehBtis7P9KsakYWIBYEaVkLnZs2a4mn1QSCPy76aYZseQE6eR9DmQZ8wy3mwkfkzk6UB7ErFRkU7NWEDVUrD0ObieQOQBv2jFowPgdjAc8mffZnI924OvuwRy72spJZducSa5T2Zz0/Ek0F6OXr1FV+gf3kgAgYdYYZeW6CCOTzWPyYcaQDDEVXiecy72wqPiLJLNXqnfUDxyXdECc/dtZqyg5DcppvMwiFdJqym5/hFpmPKwfMGva6mQp8ZdnBXTxRdSNsQJaI8gOE/EJNcJjiag6H0rGETS4HPiv7Rt7HzXDgy1w1U/S6IbX81o1FqG2sLvVeLxRpVy6tmkT5kFJOIfHiJwR6nsH+KLYQANgyV6ZHXUgQ/Lpq1L6WNyeBX6HnfWNgATOIeVV19cwQtmvsjSny0TjMXL6mR6Bt+4qYr3EZrd2q1nwI="


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