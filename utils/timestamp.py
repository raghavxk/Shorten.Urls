import datetime


def get_hour_from_timestamp(posix_time):
    return datetime.datetime.utcfromtimestamp(posix_time).strftime('%H')
