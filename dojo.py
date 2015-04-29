import random
from noise import pnoise1
from pysynth_e import *

base = random.randint(0, 255)

bands = ['c', 'd', 'e', 'f', 'g', 'a', 'bb', 'c#', 'd', 'eb', 'f#', 'g', 'a', 'b']
METRE_CHOICES = ['2/2', '2/4', '3/4', '4/4', '6/8']


def wave():

    return [int(pnoise1((i/100.0) * 15, 4) * 100) for i in range(0, 128)]


def convert_wave(wave):

    bandrange = max(wave) / (len(bands) - 1)
    return [bands[(point/bandrange) -1] for point in wave if point > 0]


def generate_abc():

    notes = convert_wave(wave())

    return tuple([(note, random.randint(2, 6)) for note in notes])


song = generate_abc()
make_wav(song, fn='test{}.wav'.format(base), bpm=140)

