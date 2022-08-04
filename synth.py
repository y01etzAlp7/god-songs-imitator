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
        self.samplerate = 44100 / 2
        self.samples = []

        self.attack_samples = 100

    def write_to_file(self, filename):
        f = wave.open(filename, "w")
        self.filter()
        f.setparams((1, 2, self.samplerate, len(self.samples), "NONE", ""))
        f.writeframes(b"".join(
            [struct.pack('<h', round(x * 32767)) for x in self.samples]))
        f.close()

    def filter(self):
        for i in range(len(self.samples) - 2):
            avg = (self.samples[i] + self.samples[i+1] + self.samples[i+2]) / 3
            self.samples[i] = (self.samples[i] + avg) / 3
                
    def sine_gen(self, freq, t):
        return math.sin(2 * math.pi * freq * t / self.samplerate)

    def square_gen(self, freq, t):
        val = self.sine_gen(freq, t)
        if val < 0:
            return -0.5
        else:
            return 0.5

    def octave_gen(self, freq, t):
        return self.sine_gen(freq, t) / 2 + self.sine_gen(freq/2, t) / 2

    # 1 1
    # 2 0.5
    # 3 0.25
    def scale_bank_gen(self, freq, t, scale):
        result = 0
        for i in range(len(scale)):
            result += self.sine_gen(freq * (i+1), t) * scale[i]
        return result

    def to_samples(self, sec):
        return sec * self.samplerate

    def add_note(self, freq, length):
        s_amt = self.to_samples(length)
        for t in range(int(s_amt)):
            result = 0.5 * self.square_gen(freq, t)
            self.samples.append(result)


    def add_rest(self, length):
        s_amt = self.to_samples(length)
        for t in range(int(s_amt)):
            self.samples.append(0)

