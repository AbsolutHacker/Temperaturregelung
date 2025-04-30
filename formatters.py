import time


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
        ==== {datetime} ====
        Temperatur: {temperature:.2f} °C
        Luftfeuchte: {relative_humidity}% r.F.
        Luftdruck: {pressure} hPa
        """.format(
            datetime=time.strftime('%H:%M:%S %d.%m.%Y', datetime),
            temperature=temperature,
            relative_humidity=int(relative_humidity),
            pressure=int(pressure)
        )

        return result


class CSVFormatter:
    def format(self, datetime, temperature, relative_humidity, pressure):
        return f"{time.strftime('%Y-%m-%d %H:%M:%S', datetime)};{temperature};{relative_humidity};{pressure}"
