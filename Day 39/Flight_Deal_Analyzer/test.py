from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

print(tomorrow, six_month_from_today)