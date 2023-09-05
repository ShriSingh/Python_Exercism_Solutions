"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    # Product of temperature and neutrons emitted per second
    product = temperature * neutrons_emitted
    # Checking the reactor against the given conditions and returning the status
    return bool(temperature < 800 and neutrons_emitted > 500 and product < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    # Calculation of generated power
    generated_power = voltage * current
    # Calculation for reaction efficiency's percentage
    efficiency_rate = (generated_power / theoretical_max_power) * 100
    # Checking the reactor for its efficiency zones
    if efficiency_rate >= 80: # 80% or more
        result = "green"
    elif 60 <= efficiency_rate < 80: # Less than 80 but at least 60%
        result = "orange"
    elif 30 <= efficiency_rate < 60: # Less than 60 but at least 30%
        result = "red"
    elif efficiency_rate < 30: # Less than 30%
        result = "black"
    # Returning the result after checking the conditions
    return result


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    # Calculated the the product of the temperature and neutrons per second
    product = temperature * neutrons_produced_per_second
    # Creating a variable to store the status
    status = "DANGER"
    # Checking the product against the percentages of thresholds
    if product < (0.9 * threshold): # --> if the product is lower than 90% of the threshold
        status = "LOW" 
    elif (0.90 * threshold) < product < (1.10 * threshold): # --> if the product is greater than 90% but lower than 110% of the threshold
        status = "NORMAL"
    # Returning the danger status of the reactor
    return status
