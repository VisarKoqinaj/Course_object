import pytest


def calculate_wage(rate:float,hour:float)->float:
    if hour<=40:
        return hour*rate
    else:
        return 40*rate + (hour-40)*1.5*rate


def test_calculate_wage():
    assert calculate_wage(10,20) == 30