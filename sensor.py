class BME280Sensor:
    def __init__(self, iio_device_number: int = 0):
        print(f'Initialisiere Sensor BME280 mit Gerätenummer {iio_device_number}')
        self.base_path = f'/sys/bus/iio/devices/iio:device{iio_device_number}/'

    def read_float(self, filename: str):
        with open(self.base_path + filename, 'r') as file:
            temp_string = file.read().replace('\n', '')
            return float(temp_string)

    def read_temperature(self) -> float:
        return self.read_float('in_temp_input')

    def read_pressure(self) -> float:
        return self.read_float('in_pressure_input')

    def read_humidity(self) -> float:
        return self.read_float('in_humidityrelative_input')

    def destroy(self):
        pass