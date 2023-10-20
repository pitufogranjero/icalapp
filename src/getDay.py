from datetime import timedelta
import datetime

def getDay(delta):
    actual_date = datetime.datetime.today()
    date_modified = actual_date + timedelta(days=delta)
    date_str = date_modified.strftime('%Y%m%d')
    print(date_str)
    return date_str
