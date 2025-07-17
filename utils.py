from datetime import datetime, timedelta
import pytz

def get_yesterday_bounds():
    tz = pytz.timezone("America/Los_Angeles")  # or your timezone
    now = datetime.now(tz)
    start_of_today = tz.localize(datetime(now.year, now.month, now.day))
    start_of_yesterday = start_of_today - timedelta(days=1)
    # Return UTC timestamps for filtering
    return start_of_yesterday.astimezone(pytz.utc), start_of_today.astimezone(pytz.utc)
