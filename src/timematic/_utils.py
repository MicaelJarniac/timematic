from datetime import time, timedelta

from .constants import S_IN_H, S_IN_MIN, US_IN_S
from .units import Microseconds


def time_in_microseconds(time: time) -> Microseconds:
    return Microseconds(
        (time.hour * S_IN_H + time.minute * S_IN_MIN + time.second) * US_IN_S
        + time.microsecond
    )


def subtract_times(first: time, second: time) -> timedelta:
    # Subtract two times
    assert first.tzinfo == second.tzinfo, "Timezones must match"
    return timedelta(
        microseconds=time_in_microseconds(first) - time_in_microseconds(second)
    )
