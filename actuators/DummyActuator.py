class DummyActuator:
    def __init__(self):
        print('Initialisiere Dummy-Aktor')

    def set_state(self, off):
        print(f"DummyAktor.schalte({'aus' if off else 'an'})")

    def destroy(self):
        print('Vernichte Dummy-Aktor')
