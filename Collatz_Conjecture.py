def steps(number):
    # Setting up a variable to store the number of steps required to reach 1
    step_counter = 0
    # Checking if the value entered is less than or equal to 0
    if number < 0 or number == 0:
        # Raising an exception
        raise ValueError("Only positive integers are allowed")
    else: # --> Runs the code below if the number entered is 1 or greater than 1
        # Running a loop while the number remains greater than 1
        while number > 1:
            # Checking if the number is even
            if number % 2 == 0:
                # Divides the number by 2 indefinitely
                number /= 2
                # Increments the count whenever the division above is done
                step_counter += 1
            else: # Runs the code below for odd numbers
                # Multiplies the number by 3 and adds 1 indefinitely
                number = (3 * number) + 1
                # Increments the count whenever the process above is done
                step_counter += 1
    # Returning the final value or total number of steps
    return step_counter
