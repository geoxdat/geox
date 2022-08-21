from datetime import datetime


def convert_iso_8601_to_datetime(datetime_str: str) -> datetime:
    '''time converter'''
    try:
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f")
        
    except ValueError as e:
        datetime_obj = None
        
    return datetime_obj