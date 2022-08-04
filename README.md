# Simple imitation of God Songs from TempleOS

This program is capable of creating music files with semi-random melodies
and rhythm patterns, just like in TempleOS.
I followed [this interpretation](https://www.youtube.com/watch?v=sabX-UqC3DY) when writing the program. 

### Parameters of sound generation:

TUNE: Simple, Normal, Complex

RESTS: Off, On

TIME SIGNATURE**: 4/4, 6/8

BPM: 141 (?)

KEY: C major (Gn - Gn+1) for n-th octave

The song alvays have 2 distinct sections named A and B.
Normal song structure: A-A-B-B (?)

### Rhythmic patterns:

- 1/4 note                   (Simple, Normal, Complex)
- Set of 2 1/8 notes         (Simple, Normal, Complex)
- Set of 3 triplet 1/8 notes (        Normal, Complex)
- Set of 4 1/16 notes        (        Normal, Complex)
- 1/8 + 2 x 1/16 pattern     (                Complex)
- 2 x 1/16 + 1/8 pattern     (                Complex)
- Dotted 1/8 + 1/16          (                Complex)

In the set of 4 1/16 notes, 1 and 3 note is same, 2 and 4 is same too.

### Progress:

- [x] All rhythmic patterns
- [x] 2 theme melody structure
- [ ] Tune choice
- [x] Rests choice 
- [ ] 6/8 Time signature

### Usage

```shell
python gen.py
```
