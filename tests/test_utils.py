from datetime import time, timedelta
from typing import Tuple

import pytest

from timematic.utils import subtract_times, time_in_microseconds


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (time(0), 0),
        (time(1), 3.6e9),
        (time(5), 1.8e10),
        (time(2, 30), 9e9),
        (time(minute=12), 7.2e8),
    ],
)
def test_time_in_microseconds(test_input: time, expected: float):
    assert time_in_microseconds(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((time(0), time(0)), timedelta(0)),
        ((time(0), time(1)), timedelta(hours=-1)),
        ((time(1), time(0)), timedelta(hours=1)),
        ((time(0), time(2)), timedelta(hours=-2)),
        ((time(2), time(0)), timedelta(hours=2)),
        ((time(minute=12), time(minute=12)), timedelta(0)),
        ((time(minute=12), time(minute=13)), timedelta(minutes=-1)),
        ((time(minute=13), time(minute=12)), timedelta(minutes=1)),
    ],
)
def test_subtract_times(test_input: Tuple[time, time], expected: timedelta):
    assert subtract_times(*test_input) == expected
