interval_in_s = 10


def should_switch_off_for_temp(temperature: float) -> bool:
    return temperature < 25 # testing value, replace before production