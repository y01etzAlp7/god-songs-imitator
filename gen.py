from random import choice, randint
import synth

patterns = ["1x1/4", "2x1/8"]
BPM = 60
BEAT_LEN_IN_SEC = 60 / BPM

class MusicNote():
    def __init__(self, lenght, using_rests):
        if using_rests:
            self.kind = choice(["Note", "Rest"])
        else:
            self.kind = "Note"

        self.note = ""
        if self.kind == "Note":
            self.note = randint(0, 7)
        self.length = lenght
    
    def __repr__(self):
        return f"{self.kind}|{self.note:2}|{self.length:5.4f}"

class RhythmStructure():
    def __init__(self, using_rests):
        self.kind = choice(patterns)

        self.notes = []

        if self.kind == "1x1/4":
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 4, using_rests))
        if self.kind == "2x1/8":
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 8, using_rests))
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 8, using_rests))
    
    def __repr__(self):
        out = "Pattern " + self.kind + ":\n"
        for note in self.notes:
            out += str(note) + "\n"
        return out

class Melody():
    def __init__(self, using_rests):
        self.patterns = []
        self.pattA = []
        self.pattB = []
        for quarter in range(0, 7):
            self.pattA.append(RhythmStructure(using_rests))
        for quarter in range(0, 7):
            self.pattB.append(RhythmStructure(using_rests))
        self.patterns = self.pattA + self.pattA + self.pattB + self.pattB

    def __repr__(self):
        out = "MELODY:\n"
        for pattern in self.patterns:
            out += repr(pattern)
        return out

    def run_synth(self):
        s = synth.WaveGen()
        for pattern in self.patterns:
            for i in pattern.notes:
                if i.kind == "Note":
                    s.add_note(synth.NOTES[i.note], i.length)
                elif i.kind == "Rest":
                    s.add_rest(i.length)
        s.write_to_file("melody.wav")

mel = Melody(False)
mel.run_synth()
