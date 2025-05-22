import log
import gpiod


log.debug(f'GPIOD-Version: {gpiod.__version__}')


class RelayActuator:
    def __init__(self, out_pin: int = 23):
        log.debug(f'Initialisiere Relais-Aktor auf GPIO-PIN {out_pin}')
        chip = gpiod.Chip('gpiochip4')
        self.relay_line = chip.get_line(out_pin)
        self.relay_line.request(consumer="Relay", type=gpiod.LINE_REQ_DIR_OUT)

    def set_state(self, off):
        log.debug(f"RelaisAktor.schalte({'aus' if off else 'an'})")
        # relay is configured as connector, so 1 means on
        self.relay_line.set_value(0 if off else 1)

    def destroy(self):
        log.debug("Vernichte Relais-Aktor")
        self.relay_line.release()
