def convert(number):
    '''
    Solving the function using solely conditional statements
    '''
    # Checking if the number is divisible by 3, 5, and 7
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return "PlingPlangPlong"
    elif number % 3 == 0 and number % 5 == 0: # If its only divisible by 3 & 5
        return "PlingPlang"
    elif number % 5 == 0 and number % 7 == 0: # If its only divisible by 5 & 7
        return "PlangPlong"
    elif number % 3 == 0 and number % 7 == 0: # If its only divisible by 3 & 7
        return "PlingPlong"
    elif number % 3 == 0: # If its only divisible by only 3
        return "Pling"
    elif number % 5 == 0: # If its only divisible by only 5
        return "Plang"
    elif number % 7 == 0: # If its only divisible by only 7
        return "Plong"
    # Returns the number in a string form if it's not divisible by 3, 5, nor 7
    return str(number)