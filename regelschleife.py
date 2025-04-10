import time
import sensor as sensor_module
import RelayActuator as relay
import rules

def main():
    print('Initialisiere Sensor')
    sensor = sensor_module.BME280Sensor()

    print('Initialisiere Aktoren...')
    actuators = [ relay.RelayActuator() ] #, ZigbeeActuator() ]

    # actuators are on per default
    last_actuator_on_state = True
    while True:
        temperature = sensor.read_temperature()
        print(f'Temperatur: {temperature:.2f} °C')
        switch_off = rules.should_switch_off_for_temp(temperature)
        if switch_off == last_actuator_on_state:
            for actuator in actuators:
                actuator.set_state(switch_off)
            last_actuator_on_state = not switch_off
        time.sleep(rules.interval_in_s)

if __name__ == '__main__':
    main()