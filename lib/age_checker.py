from datetime import datetime

def age_checker(string, value):
    #Check the input type
    if not isinstance(string, str):
        return "Date format incorrect"
    #Now checking format
    try:
        dob = datetime.strptime(string, "%Y-%m-%d")
    except ValueError:
        return "Date format incorrect"
    #Work out age
    today = datetime(2025, 10, 21)
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    #And then compare with minimum value
    if age < value:
        return f"Access denied! You are {age} years old. Minimum age is {value}."
    else:
        return "Access granted!"