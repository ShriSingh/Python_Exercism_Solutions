def equilateral(sides):
    '''
    Checks if the sides of the triangle make it equilateral
    '''
    # Checking if the sides are a triangle through the triangle_check()
    checking_shape = triangle_check(sides)
    # Checking the output of the function
    if checking_shape is not True:
        # If the shape is not a triangle, then it cannot be a equilateral triangle
        return False

    # Assigning the sides of the shape to a variable
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]

    # Checking the sides against the requirements of an equilateral triangle
    equilateral_check = side_a == side_b == side_c
    # Returning the boolean value after checking the sides
    return equilateral_check


def isosceles(sides):
    '''
    Checks if the sides of the triangle make it isoceles
    '''
    # Checking if the sides are a triangle through the triangle_check()
    checking_shape = triangle_check(sides)
    # Checking the output of the function
    if checking_shape is not True:
        # If the shape is not a triangle, then it cannot be an isosceles triangle
        return False

    # Assigning the sides of the shape to a variable
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]

    # Checking the sides against the requirements of an isosceles triangle
    isosceles_check = side_a == side_b or side_b == side_c or side_a == side_c
    # Returning the boolean value after checking the sides
    return isosceles_check


def scalene(sides):
    '''
    Checks if the sides of the triangle make it scalene
    '''
    # Checking if the sides are a triangle through the triangle_check()
    checking_shape = triangle_check(sides)
    # Checking the output of the function
    if checking_shape is not True:
        # If the shape is not a triangle, then it cannot be a scalene triangle
        return False

    # Assigning the sides of the shape to a variable
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]

    # Checking the sides against the requirements of a scalene triangle
    scalene_check = side_a != side_b and side_b != side_c and side_a != side_c
    # Returning the boolean value after checking the sides
    return scalene_check


def triangle_check(sides):
    """
    Checks if the sides of the shape make it a triangle or not
    """
    # Iterates through the sides of the shape in the given list
    for side in sides:
        # Checks if any of the sides is 0
        if side <= 0:
            # If the condition is met, return false
            return False

    # Assigning the sides of the shape to a variable
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]

    # Checking the sides against the expressions
    if side_a + side_b >= side_c and side_b + side_c >= side_a and side_a + side_c >= side_b:
        # Returning true if the expressions are true
        return True

    # Returning the default response
    return False
