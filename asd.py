import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import random
SCOPES = ['https://www.googleapis.com/auth/calendar.events']


def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        event = {
            "summary": "saaaa",
            "location": "Somewhere Online",
            "description": "Some more details on this awesome event",
            "colorId": random.randint(1, 11),
            "start": {
                "dateTime": "2023-10-11T09:00:00+02:00",
                "timeZone": "Europe/Vienna"
            },
            "end": {
                "dateTime": "2023-10-11T17:00:00+02:00",
                "timeZone": "Europe/Vienna"
            },
            "recurrence": [
                "RRULE:FREQ=DAILY;COUNT=1"  # Updated COUNT to 1 for a single event
            ],
            "attendees": [
                {"email": "cdiscolc21@gmail.com"},
                {"email": "someemailthathopefullydoesnotexist@mail.com"}
            ]
        }
        event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")

    except HttpError as error:
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
