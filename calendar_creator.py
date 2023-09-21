import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
import re
import random
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

class CalendarEventCreator:
    def __init__(self):
        self.summary = None
        self.description = None
        self.startDate = None
        self.startTime = None
        self.endDate = None
        self.endTime = None
        self.attendees = None

        self.prompt_for_missing_fields()

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
                "summary": self.summary,
                "description": self.description,
                "colorId": random.randint(1, 11),
                "start": {
                    "dateTime": f"{self.startDate}T{self.startTime}:00+03:00",
                    "timeZone": "Europe/Chisinau"
                },
                "end": {
                    "dateTime": f"{self.endDate}T{self.endTime}:00+03:00",
                    "timeZone": "Europe/Chisinau"
                },

                # Use the attendees list here
                "attendees": [{"email": email.strip()} for email in self.attendees.split(',')]
            }
            event = service.events().insert(calendarId="primary", body=event).execute()
            print(f"Event created: {event.get('htmlLink')}")

        except HttpError as error:
            print(f'An error occurred: {error}')

    def validate_datetime_format(self, datetime_str):
        try:
            datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            return True
        except ValueError:
            return False

    def validate_email_format(self, email_str):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_pattern, email_str) is not None

    def prompt_for_missing_fields(self):
        if not self.summary:
            self.summary = input("What is the meeting about? ")
        if not self.description:
            self.description = input("Description: ")
        while not self.startDate or not self.validate_datetime_format(f"{self.startDate} 00:00"):
            self.startDate = input("Start date (YYYY-MM-DD): ")
        if not self.startTime:
            self.startTime = input("Start time (HH:MM): ")
            while not self.validate_datetime_format(f"{self.startDate} {self.startTime}"):
                print("Invalid date or time format. Please use YYYY-MM-DD HH:MM.")
                self.startTime = input("Start time (HH:MM): ")
        while not self.endDate or not self.validate_datetime_format(f"{self.endDate} 00:00"):
            self.endDate = input("End date (YYYY-MM-DD): ")
        if not self.endTime:
            self.endTime = input("End time (HH:MM): ")
            while not self.validate_datetime_format(f"{self.endDate} {self.endTime}"):
                print("Invalid date or time format. Please use YYYY-MM-DD HH:MM.")
                self.endTime = input("End time (HH:MM): ")
        while not self.attendees or not all(self.validate_email_format(email.strip()) for email in self.attendees.split(',')):
            attendees_input = input("Enter a comma-separated list of attendees' email addresses: ")
            self.attendees = attendees_input.strip()

# Usage example:
creator = CalendarEventCreator()
