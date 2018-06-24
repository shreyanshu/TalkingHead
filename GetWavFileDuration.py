
import wave
import contextlib


    # fname = 'goforward2.wav'

def get_length(fname):
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return(duration)
