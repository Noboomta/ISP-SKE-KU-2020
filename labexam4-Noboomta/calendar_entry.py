from datetime import datetime, time


# Extract Method of the duplicated code in 3 classes.
def instance_check(date: str, str: str) -> str:
    """ return the date if it not raise the ValueError."""
    if isinstance(date, str):
        try:
            if '/' in date:
                date = datetime.strptime(date, "%d/%m/%Y")
            elif '-' in date:
                # try both yyyy-mm-dd and dd-mm-yyyy
                try:
                    date = datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    date = datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            # rethrow with a helpful message
            raise ValueError(f"Unrecognized date string: {date}. Use d/m/y or y-m-d.")
    return date
    
class CalendarEntry:
    """A calendar entry for a special date, event, or meeting."""

    # extract method at super class.
    def generate_time(self, start_time: str, end_time: str) -> None:
        """ Set the parameter to be a Time."""
        if start_time:
            hms = [int(value) for value in start_time.split(':')]
            start_time = time(*hms)
        if end_time:
            hms = [int(value) for value in end_time.split(':')]
            end_time = time(*hms)
        elif start_time:
            end_time = time(start_time.hour+1, start_time.minute, start_time.second)
        self._starttime = start_time
        self._endtime = end_time

    @property
    def description(self) -> str:
        """The description of this calendar entry."""
        return self._description
    
    @property
    def date(self) -> datetime:
        """The date of this calendar entry as a date object without the time."""
        return self._date.date()
    
    @property
    def start_time(self) -> time:
        """The starting time of an event or meeting."""
        return self._starttime
    
    @property
    def end_time(self) -> time:
        """The ending time of an event or meeting."""
        return self._endtime


class DateEntry(CalendarEntry):
    """ subclass of the DateEntry inherit from CalendarEntry."""
    def __init__(self, description, date: str) -> None:
        """Initialize a new event.

        Arguments:
        description - description of this calendar entry
        date - the date when the entry occurs. May be a datetime object or string in form d/m/y or y-m-d.
        """
        self._description = description
        self._date = instance_check(date, str)

    def __str__(self) -> str:
        return self.description
    

class EventEntry(CalendarEntry):
    """ subclass of the EventEntry inherit from CalendarEntry."""
    def __init__(self, description: str, date: str, start_time: str = None, end_time: str = None) -> None:
        """Initialize a new event.

        Arguments:
        description - description of this calendar entry
        date - the date when the entry occurs. May be a datetime object or string in form d/m/y or y-m-d.
        start_time - start time for a meeting or event. Only for EVENT and MEETING types.
        end_time   - end time for a meeting or event. Only for EVENT and MEETING types.
        """
        self._description = description
        self._date = instance_check(date, str)

        # Duplicate code and long code - Extract method.
        self.generate_time(start_time, end_time)

        self._date = datetime.combine(self._date, self._starttime)
    
    def __str__(self) -> str:
        return f"{self.start_time:%H:%M}-{self.end_time:%H:%M}: {self.description}"


class MeetingEntry(CalendarEntry):
    """ subclass of the MeetingEntry inherit from CalendarEntry."""
    def __init__(self, description: str, date: str, start_time: str = None, end_time: str = None) -> None:
        """Initialize a new meeting.

        Arguments:
        description - description of this calendar entry
        date - the date when the entry occurs. May be a datetime object or string in form d/m/y or y-m-d.
        start_time - start time for a meeting or event. Only for EVENT and MEETING types.
        end_time   - end time for a meeting or event. Only for EVENT and MEETING types.
        """
        self._description = description
        self._date = instance_check(date, str)

        # Duplicate code and long code - Extract method.
        self.generate_time(start_time, end_time)

        self._date = datetime.combine(self._date, self._starttime)
        self.attendees = []

    def add_attendee(self, name: str) -> None:
        """Add an attendee to a meeting."""
        self.attendees.append(name)
    
    def __str__(self) -> str:
        if len(self.attendees) == 0:
            others = "no others"
        else:
            others = ", ".join(self.attendees[:3]) # show first 3
            if len(self.attendees) > 3:
                others += f" and {len(self.attendees)-3} others"
        return f"{self.start_time:%H:%M}-{self.end_time:%H:%M}: {self.description} with {others}"