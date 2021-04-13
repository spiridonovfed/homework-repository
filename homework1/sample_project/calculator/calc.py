import math


def check_power_of_2(a: int) -> bool:
    return int(math.sqrt(a)) == float(math.sqrt(a))
