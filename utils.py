from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo  # Python 3.9+

def get_yesterday_bounds():
    tz = ZoneInfo("America/Los_Angeles")  # <-- Change this to your actual timezone
    now = datetime.now(tz)
    start_of_today = datetime(year=now.year, month=now.month, day=now.day, tzinfo=tz)
    start_of_yesterday = start_of_today - timedelta(days=1)
    # Convert to UTC for comparison
    return start_of_yesterday.astimezone(timezone.utc), start_of_today.astimezone(timezone.utc)
