# This part will generate wav file from the given sequence of notes and rests.
import math
import wave
import struct

# From G4 to G5 in C major key
NOTES = [
    391.9954, 440.0000, 493.8833, 523.2511, 
    587.3295, 659.2551, 698.4565, 783.9909
]

class WaveGen():
    def __init__(self):
        self.samplerate = 44100
        self.samples = []

    def write_to_file(self, filename):
        f = wave.open(filename, "w")
        f.setparams((1, 2, self.samplerate, len(self.samples), "NONE", ""))
        f.writeframes(b"".join(
            [struct.pack('<h', round(x * 32767)) for x in self.samples]))
        f.close()

    def sine_gen(self, freq, t):
        return math.sin(2 * math.pi * freq * t / self.samplerate)

    def to_samples(self, sec):
        return sec * self.samplerate

    def add_note(self, freq, length):
        s_amt = self.to_samples(length)
        for t in range(int(s_amt)):
            self.samples.append(0.5 * self.sine_gen(freq, t))

    def add_rest(self, length):
        s_amt = self.to_samples(length)
        for t in range(int(s_amt)):
            self.samples.append(0)

