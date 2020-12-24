"""A simple calendar.  
We use the name 'cal' instead of 'calendar' to avoid
conflict with Python library module named 'calendar'.
"""
from typing import List
import calendar_entry
from datetime import date, datetime


class Cal:

    @classmethod
    def create_date(cls, description: str, date: str):
        """Make a new DATE item."""
        entry = calendar_entry.DateEntry(description, date)
        return entry

    @classmethod
    def create_event(cls, description: str, date: str, start_time: str, end_time: str):
        """Make a new Event item."""
        event = calendar_entry.EventEntry(description, date,
                 start_time, end_time)
        return event
    
    @classmethod
    def create_meeting(cls, description: str, date: str, start_time: str, end_time: str, *attendees: List[str]) -> calendar_entry.EventEntry:
        """Make a new Meeting item."""
        event = calendar_entry.MeetingEntry(description, date,
                 start_time, end_time)
        for attendee in attendees:
            event.add_attendee(attendee)
        return event
    
    def __init__(self, name: str) -> None:
        """Initialize a new calendar. 

        Arguments:
        name - the name for this calendar.
        """
        self._name = name
        self.entries = []
    
    def add(self, item: calendar_entry.CalendarEntry) -> None:
        """Add a CalendarEntry to this calendar."""
        self.entries.append(item)

    @property
    def name(self) -> str:
        return self._name

    def is_today(self, event: calendar_entry.EventEntry) -> date:
        """Test if a calendar entry occurs today.

        Arguments:
        event - a CalendarEntry instance

        Returns: True if the event is today, False otherwise
        """
        return datetime.today().date() == event._date.date()
