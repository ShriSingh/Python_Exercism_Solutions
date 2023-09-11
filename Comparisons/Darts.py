def score(x, y):
    """
    Determining the points earned in a single toss of a Dart
    """
    # Basic Equation of a Circle: x^2 + y^2 = r^2
    # Variable to store and output points scored
    points_earned = 0
    # Noting down the units of radii of the circles
    outer_circle_radius = 10
    middle_circle_radius = 5
    inner_circle_radius = 1
    # Storing the sum of the squares of the coordinate positions
    sum_of_squares = (x ** 2) + (y ** 2)
    # Storing the distance from the center by square rooting the sum of squares
    # Square root is essentially raising by 1/2
    coordinate_length = sum_of_squares ** 0.5
    # Comparing the corrdinate length with the radii lengths
    if coordinate_length > outer_circle_radius:
        # If the distance greater than the outer circle radius
        points_earned = 0
    elif middle_circle_radius < coordinate_length <= outer_circle_radius:
        # If the distance is greater than middle circle radius
        # but smaller or equal to outer circle radius
        points_earned = 1
    elif inner_circle_radius < coordinate_length <= middle_circle_radius:
        # If the distance is greater than inner circle radius
        # but smaller or equal to middle circle radius
        points_earned = 5
    else:
        # If the distance is anything other than the conditionals above
        points_earned = 10
    # Returning the points earned by the player
    return points_earned
