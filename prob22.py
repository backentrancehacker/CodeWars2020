'''
You will receive either a fret number and a
string name (separated by a space) or you will
receive a Note name. 

If you receive a fret and
a string, output the NEXT note in the scale
(working from fret zero (open) towards fret 12;
if the next fret would go past 12, return to the
"open string" /zero fret).

If you receive a Note name, output the fret and
string (on both strings, list the E string first) the
note can be played.

Notes:
0 is used to represent the "open string", e.g.
the top of the fret board.
For those of you with musical backgrounds,
we're ignoring the sharps and flats, skip
over them like they aren't there.
If the "next" note called for is past fret 12,
you will need to "return" to the zero/"Open"
fret, but the note will stay the same. E.G. A
on fret twelve will also be A on fret zero.
'''
import time

Enote = {0: 'F', 1: 'G', 3: 'A', 5: 'B', 7: 'C', 8: 'D', 10: 'E', 12: 'E'}
Anote = {0: 'B', 2: 'C', 3: 'D', 5: 'E', 7: 'F', 8: 'G', 10: 'A', 12: 'A'}

Efret = {0: 'E', 1: 'F', 3: 'G', 5: 'A', 7: 'B', 8: 'C', 10: 'D', 12: 'E'}
Afret = {0: 'A', 2: 'B', 3: 'C', 5: 'D', 7: 'E', 8: 'F', 10: 'G', 12: 'A'}

Ekeys = list(Efret.keys())
Evalues = list(Efret.values())
Akeys = list(Afret.keys())
Avalues = list(Afret.values())

forcount = []

loopbreak = time.time() + 1
#timed loop with an exeption for the EOF error
try:
    while loopbreak > time.time():
        forcount.append(input())
except EOFError:
    count = len(forcount)
    count = int(count)
    for i in range(0, count):
        try:
            num, note = forcount[i].split()
            num = int(num)
            if note == 'A':
                print(Anote[num])
            elif note == 'E':
                print(Enote[num])
        except:
            note = forcount[i]
            note = str(note)
            if note == 'E':
                print('0 E 12 E', Akeys[Avalues.index(note)], 'A')
            elif note == 'A':
                print(Ekeys[Evalues.index(note)], 'E 0 A 12 A')
            else:
                print(Ekeys[Evalues.index(note)], 'E', Akeys[Avalues.index(note)], 'A')
