def response(hey_bob):
    # Taking all the whitespaces from the input
    talking_to_bob = hey_bob.strip()
    # Checking if all the input is in upper case as a boolean
    yelling_at_him = talking_to_bob.isupper()
    # Checking if the input ends with a question mark as a boolean
    asking_him = talking_to_bob.endswith("?")
    # Checking whether removing all whitespace from input returns nothing
    giving_silent_treatment = talking_to_bob == ""

    # Checking if you're yelling at Bob
    if yelling_at_him:
        # Checking if you're asking Bob something at the same time
        if asking_him:
            return "Calm down, I know what I'm doing!"
        else:  # If you're just yelling at him
            return "Whoa, chill out!"
    elif asking_him:  # Checking if you're just asking him something
        return "Sure."
    elif giving_silent_treatment:  # Checking if didn't saying to Bob
        return "Fine. Be that way!"

    # Returning his default response
    return "Whatever."