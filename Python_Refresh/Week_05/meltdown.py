"""
In this exercise, we'll develop a simple control system for a nuclear reactor.
"""

"""
critical condition :
The temperature is less than 800 K
The number of neutrons emitted per second is greater than 500.
The product of temperature and neutrons emitted per second is less than 500000.
"""

def is_criticality_balanced(temprature, neuron_emitted):
    """
    that takes temperature measured in kelvin and neutrons_emitted as parameters, 
    and returns True if the criticality conditions are met, False if not.
    """
    if temprature < 800 and neuron_emitted > 500 and temprature * neuron_emitted < 500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    """
    green -> efficiency of 80% or more,
    orange -> efficiency of less than 80% but at least 60%,
    red -> efficiency below 60%, but still 30% or more,
    black -> less than 30% efficient.

    """
    generated_power = voltage * current
    percent_value = (generated_power/theoretical_max_power) * 100

    if percent_value >= 80:
        return "Green"
    if 60 <= percent_value < 80:
        return "Orange"
    if 30 <= percent_value < 60:
        return "Red"
    if percent_value < 30:
        return "Black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):

    criticality = temperature * neutrons_produced_per_second
    low_threshold = 0.9 * threshold
    high_threshold = 1.1 * threshold
    if temperature * neutrons_produced_per_second < low_threshold:
        return 'LOW'
    if low_threshold <= criticality <= high_threshold:
        return 'NORMAL'
    return 'DANGER'

def main():
    result1 = is_criticality_balanced(750, 600)
    print(result1)

    result2 = reactor_efficiency(200,50,15000)
    print(result2)

    result3 = fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)
    print(result3)

main()
