import gpiod
print(f'GPIOD-Version: {gpiod.__version__}')


class RelayActuator:
    def __init__(self, out_pin: int = 23):
        print(f'Initialisiere Relais-Aktor auf GPIO-PIN {out_pin}')
        chip = gpiod.Chip('gpiochip4')
        self.relay_line = chip.get_line(out_pin)
        self.relay_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

    def set_state(self, off):
        print(f"RelaisAktor.schalte({'aus' if off else 'an'})")
        self.relay_line.set_value(1 if off else 0)

    def destroy(self):
        self.relay_line.release()
