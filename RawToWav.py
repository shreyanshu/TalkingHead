import sys
import wave


def run(fname):
    with open(fname, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    wavfile = wave.open('wavFile/test.wav', 'wb')
    wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
    wavfile.writeframes(pcmdata)

