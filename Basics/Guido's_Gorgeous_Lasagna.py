"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Defining the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time

# Defining the 'PREPARATION_TIME' constant
PREPARATION_TIME = 2
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the time required to make the layers of lasagna

    :param number_of_layers: int - the number of layers in the lasagna
    :return: int - total preparation time for all the number of layers in the lasagna

    Function that take the number of layers you add to the lasagna as an argument and returns how
    many minutes you would spend making them, assuming each layer takes 2 minutes to prepare.
    """
    total_preparation_time = PREPARATION_TIME * number_of_layers
    return total_preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna
    :param elapsed_bake_time: int - elapsed cooking time
    :return: int - total time elapsed(in minutes) preparing and cooking

    This function take two integers representing the number of lasagna layers and the time
    already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    elapsed_preparation_time = preparation_time_in_minutes(number_of_layers)
    total_elapsed_cooking_time = elapsed_preparation_time + elapsed_bake_time
    return total_elapsed_cooking_time