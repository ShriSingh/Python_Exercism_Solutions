"""
Number of grains on a given square
"""
def square(number):
    # Checking if the number entered is between the accepted range
    if number < 1 or number > 64:
        # When the square value is not in the acceptable range
        raise ValueError("square must be between 1 and 64")
    # Returning the math of 2 ^ n - 1, with 'n' being the number of a given square
    return 2 ** (number - 1)


"""
Returns the total number of grains on the chessboard
"""
def total():
    # Creating a variable to store the total grains
    total_grains = 0
    # Iterating thru number in the chessboard, 1 to 65(inclusive)
    for i in range(1, 65):
        # Running the square() and adding up the results
        total_grains += square(i)
        # Appending the loop 
        i += 1
    # Returning the total number of grains on the checkerboard
    return total_grains
