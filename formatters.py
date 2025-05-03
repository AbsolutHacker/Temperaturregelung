import time
import math


def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32


def dew_point(temp_c, relative_humidity):
    # source: https://www.wettermail.de/wetter/feuchte.html
    if temp_c < 0:
        raise ValueError("Nicht implementiert für Temperaturen unter 0 °C")
    a = 7.5
    b = 237.3
    c = 6.1078
    svp = 6.1078 * (10 ** ((a*temp_c)/(b+temp_c)))
    vp = svp * relative_humidity / 100
    v = math.log10(vp / c)
    return (b * v)/(a - v)


class ConsoleFormatter:
    def __init__(self):
        self.first_output = True

    def format(self, datetime, temperature, relative_humidity, pressure):
        if not self.first_output:
            result = '' # TODO: insert control characters to clear console
        else:
            self.first_output = False
            result = ''

        result += """
====== {datetime} ======
Temperatur:\t{temperature:.2f} °C
Temperatur:\t{temp_f:.2f} °F
Luftfeuchte:\t{relative_humidity}% r.F.
Luftdruck:\t{pressure} hPa
Taupunkt:\t{dew_point:.2f} °C
""".format(
            datetime=time.strftime('%H:%M:%S %d.%m.%Y', datetime),
            temperature=temperature,
            temp_f=celsius_to_fahrenheit(temperature),
            relative_humidity=int(relative_humidity),
            pressure=int(pressure),
            dew_point=dew_point(temperature, relative_humidity)
        )

        return result


class CSVFormatter:
    def format(self, datetime, temperature, relative_humidity, pressure):
        return f"{time.strftime('%Y-%m-%d %H:%M:%S', datetime)};{temperature};{relative_humidity};{pressure}"
