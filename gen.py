from random import choice, randint
import synth

patterns = [
    "1x1/4", "2x1/8",               # Simple tune patterns
    "3x1/8T", "4x1/16",             # Additional Normal tune patterns
    "1x1/8+2x1/16", "2x1/16+1x1/8", # Additional Complex tune patterns
    "1x1/8D+1x1/16"
    ]

BPM = 120
BEAT_LEN_IN_SEC = 60 / BPM

class MusicNote():
    def __init__(self, lenght, using_rests):
        if using_rests:
            self.kind = choice(["Note", "Rest", "Note", "Note"])
        elif not using_rests:
            self.kind = "Note"

        self.note = ""
        if self.kind == "Note":
            self.note = randint(0, 7)
        self.length = lenght
    
    def __repr__(self):
        return f"{self.kind}, {self.note:2}" # "|{self.length:5.4f}"

class RhythmStructure():
    def __init__(self, tune_complexity, using_rests):
        self.kind = choice(patterns)

        self.notes = []

        if self.kind == "1x1/4":
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC, using_rests))
        elif self.kind == "2x1/8":
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 2, using_rests))
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 2, using_rests))
        elif self.kind == "3x1/8T":
            tri_len = BEAT_LEN_IN_SEC / 3
            for i in range(0, 3):
                self.notes.append(MusicNote(tri_len, using_rests))
        elif self.kind == "4x1/16":
            LEN_1_16 = BEAT_LEN_IN_SEC / 4
            note1 = MusicNote(LEN_1_16, using_rests)
            note2 = MusicNote(LEN_1_16, using_rests)
            self.notes.append(note1)
            self.notes.append(note2)
            self.notes.append(note1)
            self.notes.append(note2)
        elif self.kind == "1x1/8+2x1/16":
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 2, using_rests))
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 4, using_rests))
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 4, using_rests))
        elif self.kind == "2x1/16+1x1/8":
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 4, using_rests))
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 4, using_rests))
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 2, using_rests))
        elif self.kind == "1x1/8D+1x1/16":
            self.notes.append(MusicNote(3 * BEAT_LEN_IN_SEC / 4, using_rests))
            self.notes.append(MusicNote(BEAT_LEN_IN_SEC / 4, using_rests))
    
    def __repr__(self):
        out = "Pattern " + self.kind + ":\n"
        for note in self.notes:
            out += "    " +  str(note) + '\n'
        return out

class Melody():
    def __init__(self, tune_complexity, using_rests):
        self.patterns = []
        self.pattA = []
        self.pattB = []
        for quarter in range(0, 15):
            self.pattA.append(RhythmStructure(tune_complexity, using_rests))
        for quarter in range(0, 15):
            self.pattB.append(RhythmStructure(tune_complexity, using_rests))
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

mel = Melody("Normal", False)
print(repr(mel))
mel.run_synth()
