def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """

    if number==1:
        i="Monday"
    elif number==2:
        i="Tuesday"
    elif number==3:
        i="Wednesday"
    elif number==4:
        i="Thursday"
    elif number==5:
        i="Friday"
    elif number==6:
        i="Saturday"
    elif number==7:
        i="Sunday"
    return i
x=main(1)
print(x)