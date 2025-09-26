from datetime import date


def validate_pesel(pesel: str):

    # Check length
    if len(pesel) != 11:
        return {"is_valid": False, "reason": "PESEL must have 11 digits"}

    # Check if PESEL contains only digits
    if not pesel.isdigit():
        return { "is_valid": False, "reason": "PESEL must contain only digits" }

    # Prepare weights and calculate weighted sum
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = 0
    for i in range(10):
        # Take only last digit of the product
        control_sum += (int(pesel[i]) * weights[i]) % 10

    # Compare check sum to control value (last PESEL digit)
    check = 10 - control_sum % 10
    is_valid = check == int(pesel[10])

    # Check if control was successful
    if not is_valid:
        return { "is_valid": False, "reason": "Control check failed" }

    # Extract birthdate
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    # Extract century from month
    if 1 <= month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        year += 2000
        month -= 20
    elif 41 <= month <= 52:
        year += 2100
        month -= 40
    elif 61 <= month <= 72:
        year += 2200
        month -= 60
    elif 81 <= month <= 92:
        year += 1800
        month -= 80
    else:
        return { "is_valid": False, "reason": "Invalid birth date" }

    # Combine final results
    birth_date = date(year, month, day)

    # Check gender
    if int(pesel[9]) % 2 == 1:
        gender = "Male"
    else:
        gender = "Female"

    return { "is_valid": True, "birth_date": birth_date, "gender": gender }
