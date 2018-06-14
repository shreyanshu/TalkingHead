import sys
import wave

with open("aajokofinaltest.raw", 'rb') as pcmfile:
    pcmdata = pcmfile.read()
wavfile = wave.open('aajokofinaltest.wav', 'wb')
wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
wavfile.writeframes(pcmdata)

