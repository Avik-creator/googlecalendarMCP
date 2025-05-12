from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime, timezone
import os.path
import pickle

from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool()
def get_all_calendar_events(start_date: str, end_date: str):
    """Get all calendar events"""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

    service = build('calendar', 'v3', credentials=creds)
    start_date = datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=timezone.utc).isoformat()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").replace(tzinfo=timezone.utc).isoformat()
    events_result = service.events().list(calendarId='avikm744@gmail.com', timeMin=start_date,
                                          timeMax=end_date,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', []) 
    return events

@mcp.tool()
def create_calendar_event(title: str, start_date: str, end_date: str, description: str):
    """Create a calendar event"""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

    service = build('calendar', 'v3', credentials=creds)
    start_date = datetime.strptime(start_date, '%Y-%m-%d').replace(tzinfo=timezone.utc).isoformat()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').replace(tzinfo=timezone.utc).isoformat()  
    event = {
        'summary': title,
        'start': {'dateTime': start_date},
        'end': {'dateTime': end_date},
        'description': description
    }
    service.events().insert(calendarId='avikm744@gmail.com', body=event).execute()
    return f"Event {title} created successfully"

@mcp.tool()
def delete_calendar_event(event_id: str):
    """Delete a calendar event"""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())    

    service = build('calendar', 'v3', credentials=creds)
    service.events().delete(calendarId='avikm744@gmail.com', eventId=event_id).execute()
    return f"Event {event_id} deleted successfully"



@mcp.tool()
def update_calendar_event(event_id: str, title: str, start_date: str, end_date: str, description: str):
    """Update a calendar event"""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)  
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

    service = build('calendar', 'v3', credentials=creds)
    start_date = datetime.strptime(start_date, '%Y-%m-%d').replace(tzinfo=timezone.utc).isoformat()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').replace(tzinfo=timezone.utc).isoformat()
    event = {
        'summary': title,
        'start': {'dateTime': start_date.isoformat()},
        'end': {'dateTime': end_date.isoformat()},
        'description': description
    }
    service.events().update(calendarId='avikm744@gmail.com', eventId=event_id, body=event).execute()   
    return f"Event {event_id} updated successfully"



if __name__ == '__main__':
    mcp.run(transport="stdio")


