def leap_year(year):
    """
    Checking if the year is "divisible by 4 'and' not divisible by 100 'or' 
    divisible by 400" 
    Alternative: Check first if the year is "divisible by 4", then check if "not divisible by 100 'or'      divisible by 400"
    If the above condition is satisfied then return True, else return False.
    """
    # Can use --> if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False