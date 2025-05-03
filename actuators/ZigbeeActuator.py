import log


class ZigbeeActuator:
    def __init__(self, device_name: str = 'steckdose'):
        import paho.mqtt.client as mqtt
        log.debug(f'Initialisiere Zigbee-Aktor')
        self.topic = f"zigbee2mqtt/{device_name}/set"
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883, 60)

    def set_state(self, off: bool):
        import json
        log.debug(f"ZigbeeAktor.schalte({'aus' if off else 'an'})")
        payload = json.dumps({'state': 'OFF' if off else 'ON'})
        self.client.publish(self.topic, payload)

    def destroy(self):
        log.debug("Vernichte Zigbee-Aktor")
        self.client.disconnect()
