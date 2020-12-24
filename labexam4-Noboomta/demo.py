"""
Demonstrate use of the Cal and CalendarEntry classes.

Creates a calendar with different kinds of items, then prints it.
"""
from cal import Cal


def print_calendar(cal):
    """Print the calendar items, sorted by date and time."""
    cal.entries.sort(key=lambda e: e._date)
    last_date = None
    print(f"{cal.name}")
    for entry in cal.entries:
        # group events by date
        if entry.date != last_date:
            day_of_week = f"({entry.date:%a})"
            # if an event occurs today, append "TODAY"
            if cal.is_today(entry):
                day_of_week += " TODAY"
            print(f"{entry.date:%d %B %Y} {day_of_week}")
            last_date = entry.date
        print(" "*2, str(entry))

holidays = """
1-1-2020,New Year's Day
1-5-2020,Labor Day
5-12-2020,Father's Day
10-12-2020,Constitution Day
25-12-2020,Christmas
31-12-2020,New Year's Eve
25-1-2020,Chinese New Year
8-2-2020,Makha Bucha
6-4-2020,Visakha Bucha
4-7-2020,Asalha Bucha
28-7-2020,King Vajiralongkon Birthday
11-12-2020,Day before ISP Final
"""

events = """
12-12-2020,10:00,16:00,ISP Final
31-1-2020,9:00,23:00,Kaset Fair (start)
8-2-2020,9:00,23:59,Kaset Fair (end)
6-4-2020,18:00,21:00,Wiang Tien ceremony at temple
7-12-2020,13:00,16:00,Software V&V Final
8-12-2020,13:00,16:00,Algorithms I Final
9-12-2020,13:00,16:00,Probability & Stats Final
9-12-2020,9:00,12:00,Interaction Design Final
13-12-2020,9:00,16:00,Simple Economics Final
18-12-2020,13:00,16:00,Networks Final
"""

meetings = """
31-12-2020,18:00,23:59,New Year's Eve Party,Nok,Dog,Meow,Pig,Rat
17-12-2020,9:00,12:00,ISP Presentations Part 1,Anusid,Arisa,Bhatara,Chanathip,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
17-12-2020,13:00,16:00,ISP Presentations Part 2,Anusid,Arisa,Bhatara,Chanathip,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
19-12-2020,18:00,21:00,End of Final Exams Party,Chayapol,Bheem,Metara,Nutta,Sahadporn,Potchara
"""

calendar = Cal("My Calendar")

# add some holidays
for data in holidays.split('\n'):
    if not data: continue
    (date, name) = data.split(',')
    holiday = Cal.create_date(name, date)
    calendar.add(holiday)

# add some events
for data in events.split('\n'):
    if not data: continue
    (date, start, end, name) = data.split(',')
    event = Cal.create_event(name, date, start, end)
    calendar.add(event)

# add some meetings with other people
for data in meetings.split('\n'):
    if not data: continue
    (date, start, end, name, *attendees) = data.split(',')
    meeting = Cal.create_meeting(name, date, start, end, *attendees)
    calendar.add(meeting)

print_calendar(calendar)
