from datetime import datetime
from dateutil.relativedelta import relativedelta

"""now = datetime.now()
yesterday = now.date() - relativedelta(days=1)
print(yesterday)"""

def filter_time(df, days=0):
    last_day = df.index[0].date()
    start_day = last_day - relativedelta(days=days)
    df = df.sort_index().loc[start_day:last_day] # sortindex to circumvent warning
    return df