from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
track2=MidiTrack()
track3=MidiTrack()
mid.tracks.append(track)
mid.tracks.append(track2)
mid.tracks.append(track3)

track.append(Message('program_change',channel=1, program=0, time=0))
track.append(Message('note_on', note=57, channel=1,velocity=127, time=4000))       # 2
track2.append(Message('note_on', note=60,channel=1, velocity=127, time=4000))
track3.append(Message('note_on', note=64,channel=1, velocity=127, time=4000))
track.append(Message('note_off', note=57,channel=1, velocity=127, time=4000))
track2.append(Message('note_off', note=60,channel=1, velocity=127, time=4000))
track3.append(Message('note_off', note=64,channel=1, velocity=127, time=4000))
track.append(Message('note_on', note=55, channel=1,velocity=127, time=0))       # 3
track2.append(Message('note_on', note=59,channel=1, velocity=127, time=0))
track3.append(Message('note_on', note=62,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=4000))
track2.append(Message('note_off', note=59,channel=1, velocity=127, time=4000))
track3.append(Message('note_off', note=62,channel=1, velocity=127, time=4000))
track.append(Message('note_on', note=53, channel=1,velocity=127, time=0))       # 4
track2.append(Message('note_on', note=57,channel=1, velocity=127, time=0))
track3.append(Message('note_on', note=60,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=4000))
track2.append(Message('note_off', note=57,channel=1, velocity=127, time=4000))
track3.append(Message('note_off', note=60,channel=1, velocity=127, time=4000))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       # 5
track2.append(Message('note_on', note=52,channel=1, velocity=127, time=0))
track3.append(Message('note_on', note=55,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=48,channel=1, velocity=127, time=4000))
track2.append(Message('note_off', note=52,channel=1, velocity=127, time=4000))
track3.append(Message('note_off', note=55,channel=1, velocity=127, time=4000))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))       # 6
track2.append(Message('note_on', note=53,channel=1, velocity=127, time=0))
track3.append(Message('note_on', note=57,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=4000))
track2.append(Message('note_off', note=53,channel=1, velocity=127, time=4000))
track3.append(Message('note_off', note=57,channel=1, velocity=127, time=4000))
track.append(Message('note_on', note=48, channel=1,velocity=127, time=0))       # 7
track2.append(Message('note_on', note=52,channel=1, velocity=127, time=0))
track3.append(Message('note_on', note=55,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=48,channel=1, velocity=127, time=4000))
track2.append(Message('note_off', note=52,channel=1, velocity=127, time=4000))
track3.append(Message('note_off', note=55,channel=1, velocity=127, time=4000))
track.append(Message('note_on', note=50, channel=1,velocity=127, time=0))       # 8
track2.append(Message('note_on', note=53,channel=1, velocity=127, time=0))
track3.append(Message('note_on', note=57,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=4000))
track2.append(Message('note_off', note=53,channel=1, velocity=127, time=4000))
track3.append(Message('note_off', note=57,channel=1, velocity=127, time=4000))
track.append(Message('note_on', note=52, channel=1,velocity=127, time=0))       # 9
track2.append(Message('note_on', note=56,channel=1, velocity=127, time=0))
track3.append(Message('note_on', note=59,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=4000))
track2.append(Message('note_off', note=56,channel=1, velocity=127, time=4000))
track3.append(Message('note_off', note=59,channel=1, velocity=127, time=4000))
track.append(Message('note_on', note=45,channel=1, velocity=127, time=0))       #10
track.append(Message('note_off', note=45,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=48,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=48,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=52,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=48,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=48,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=43,channel=1, velocity=127, time=0))       #11
track.append(Message('note_off', note=43,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=47,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=47,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=50,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=47,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=47,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=41,channel=1, velocity=127, time=0))       #12
track.append(Message('note_off', note=41,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=45,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=45,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=48,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=48,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=45,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=45,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=48,channel=1, velocity=127, time=0))       #13
track.append(Message('note_off', note=48,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=52,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=55,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=52,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=50,channel=1, velocity=127, time=0))       #14
track.append(Message('note_off', note=50,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=53,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=57,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=57,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=53,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=53,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=48,channel=1, velocity=127, time=0))       #15
track.append(Message('note_off', note=48,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=52,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=55,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=52,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=47,channel=1, velocity=127, time=0))       #16
track.append(Message('note_off', note=47,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=50,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=55,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=50,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=50,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=48,channel=1, velocity=127, time=0))       #17
track.append(Message('note_off', note=48,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=52,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=52,channel=1, velocity=127, time=1000))
track.append(Message('note_on', note=55,channel=1, velocity=127, time=0))
track.append(Message('note_off', note=55,channel=1, velocity=127, time=1000))

mid.save('./music/lemon.mid')