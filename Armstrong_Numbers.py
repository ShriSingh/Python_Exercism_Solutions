def is_armstrong_number(number):
    """
    Write a function that determines whether a number is an armstrong number. 
    An armstrong number is the sum of its own digits each to the power of 
    the number of digits.
    """
    # Storing the original number given for testing
    ORIGINAL_NUMBER = number
    # Calling the "number_of_digits" function
    nums = number_of_digits(number)
    # Creating a variable to store the sum of its own digits each to the power of the number of digits
    total_sum = 0 
    # Creating another while loop to run until the number is reduced to '0'
    while number > 0:
        decimal_digit = number % 10 # --> Tells the value to the right of the decimal
        number //= 10 # --> Moves the decimal to the left
        total_sum += pow(decimal_digit, nums) # --> Sums up the exponents
    # Checking the number is an armstrong number
    if total_sum == ORIGINAL_NUMBER:
        # Returning True is total sum is equal to the original number
        return True
    else:
        # Returning False is total sum is not equal to the original number
        return False
    
def number_of_digits(num):
    # Creating a variable to store the number of digits in the number
    digit_counter = 0 # --> Initiating it as '0'
    # Creating a while loop to run until the number is reduced to '0'
    while num > 0:
        num //= 10 # --> Moves the decimal to the left: 456.0 --> 45.6
        # Incrementing the number of digits
        digit_counter += 1
    # Returning the total number of digits in the number
    return digit_counter
        