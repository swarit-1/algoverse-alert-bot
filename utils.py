from datetime import datetime, timedelta, timezone

def get_yesterday_bounds():
    now = datetime.now(timezone.utc)
    # Adjust here if you want your own timezone
    start_of_today = datetime(year=now.year, month=now.month, day=now.day, tzinfo=timezone.utc)
    start_of_yesterday = start_of_today - timedelta(days=1)
    return start_of_yesterday, start_of_today