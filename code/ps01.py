import math
import numpy as np
import thinkdsp

class SawtoothSignal(thinkdsp.Signal):
    """Represents a sawtooth signal."""
    
    def __init__(self, freq=440, amp=1.0, offset=0):
        """Initializes a sinusoidal signal.

        freq: float frequency in Hz
        amp: float amplitude, 1.0 is nominal max
        offset: float phase offset in radians
        func: function that maps phase to amplitude
        """
        self.freq = freq
        self.amp = amp
        self.offset = offset

    def func(self, ts):
        frac, _ = np.modf(ts)
        return thinkdsp.normalize(thinkdsp.unbias(frac), 1)

    @property
    def period(self):
        """Period of the signal in seconds.

        returns: float seconds
        """
        return 1.0 / self.freq

    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """
        phases = self.freq * ts + self.offset / (math.pi * 2)
        ys = self.amp * self.func(phases)
        return ys