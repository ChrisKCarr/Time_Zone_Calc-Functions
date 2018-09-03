
# coding: utf-8

# In[6]:


def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    """
    return time_2 - time_1
    


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    """
    return seconds_difference(time_1,time_2) / 3600 



def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    >>> to_float_hours(0, 15, 0)
    0.25
    """
    return hours + minutes /60 + seconds / 3600



def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    >>> to_24_hour_clock(24)
    0
    """

    return hours % 24



### Write your get_hours function definition here:

def get_hours(seconds):
    """
    (int) -> int
    
    convert seconds into hours within a 24 hour clock format.
    """
    hours = seconds // 3600
    return to_24_hour_clock(hours)


### Write your get_minutes function definition here:
def get_minutes(seconds):
    """
    (int) -> int
    
    convert seconds into minutes within a 24 hour clock format.
    
    """
    minutes  = seconds // 60
    minutes %= 60
    return minutes
### Write your get_seconds function definition here:
def get_seconds(seconds):
    """
    (int) -> int
    
    returns how many seconds there will be left over in a 24 hour clock format
    """
    seconds = seconds % 60
    return seconds

def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    """
    return float(time - utc_offset) % 24


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    """
    return float(time + utc_offset) % 24

