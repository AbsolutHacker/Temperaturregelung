import time
import sensor as sensor_module
from actuators import RelayActuator
import rules


def main():
    print('Initialisiere Sensor...')
    sensor = sensor_module.BME280Sensor()

    print('Initialisiere Aktoren...')
    actuators = [ RelayActuator() ] #, ZigbeeActuator() ]

    # actuators are on per default
    last_actuator_on_state = True
    # switch once to ensure correct state
    for actuator in actuators:
        actuator.set_state(not last_actuator_on_state)

    while True:
        try:
            temperature = sensor.read_temperature()
            print(f'Temperatur: {temperature:.2f} °C')
            switch_off = rules.should_switch_off_for_temp(temperature)
        except Exception as exception:
            print(f'[WARN] Fehler beim Auslesen des Sensors: {exception}')
            print(f'[WARN] -> Kühlung an')
            switch_off = False
        if switch_off == last_actuator_on_state:
            for actuator in actuators:
                actuator.set_state(switch_off)
            last_actuator_on_state = not switch_off
        time.sleep(rules.interval_in_s)


if __name__ == '__main__':
    main()
