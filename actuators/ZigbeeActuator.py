import logging as log
import zigpy


class ZigbeeActuator:
    def __init__(self):
        log.debug(f'Initialisiere Zigbee-Aktor')

    def set_state(self, off):
        log.debug(f"ZigbeeAktor.schalte({'aus' if off else 'an'})")

    def destroy(self):
        pass
