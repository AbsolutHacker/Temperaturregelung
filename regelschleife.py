import time
import sys
import sensor as sensor_module
from actuators import RelayActuator
import rules
import logging as log
import formatters


def main():
    log.debug('Initialisiere Sensor...')
    sensor = sensor_module.BME280Sensor()

    log.debug('Initialisiere Aktoren...')
    actuators = [ RelayActuator() ] #, ZigbeeActuator() ]

    if len(sys.argv) > 1 and sys.argv[1] == '--csv':
        formatter = formatters.CSVFormatter()
    else:
        formatter = formatters.ConsoleFormatter()

    # actuators are on per default
    last_actuator_on_state = True
    # switch once to ensure correct state
    for actuator in actuators:
        actuator.set_state(not last_actuator_on_state)

    while True:
        try:
            temperature = sensor.read_temperature()
            humidity = sensor.read_humidity()
            pressure = sensor.read_pressure()
            datetime = time.localtime()
            log.info(formatter.format(datetime, temperature, humidity, pressure))
            switch_off = rules.should_switch_off_for_temp(temperature)
        except Exception as exception:
            log.warn(f'Fehler beim Auslesen des Sensors: {exception}')
            log.warn(f'-> Kühlung an')
            switch_off = False

        if switch_off == last_actuator_on_state:
            for actuator in actuators:
                actuator.set_state(switch_off)
            last_actuator_on_state = not switch_off

        try:
            time.sleep(rules.interval_in_s)
        except KeyboardInterrupt:
            log.debug('Unterbrechung, schalte ab')
            for actuator in actuators:
                actuator.destroy()
            break


if __name__ == '__main__':
    main()
