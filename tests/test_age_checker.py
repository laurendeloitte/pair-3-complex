from lib.age_checker import age_checker
import pytest
from datetime import datetime
"""
Check to see if a string has been entered
"""
def empty_string_input():
    result = age_checker("", 16)
    assert result == "Date format incorrect"

"""
Want to check to see if a number has been entered
and not a string
"""
def test_check_if_number_entered():
    result = age_checker(20251021, 16)
    assert result == "Date format incorrect"

"""
Check the right string and date format
has been entered but underaged
"""
def test_check_right_string_and_date_format():
    result = age_checker("2025-10-21", 16)
    #This person would be age 0 so Access Denied
    assert result == "Access denied! You are 0 years old. Minimum age is 16."

"""
Check for invalid date value(month 13 and day 40 don't exist)
"""
def test_invalid_date_value():
    result = age_checker("2025-13-40", 16)
    assert result == "Date format incorrect"

"""
Check for access granted as they are old enough
"""
def test_access_granted():
    result = age_checker("1969-05-02", 16)
    assert result == "Access granted!"