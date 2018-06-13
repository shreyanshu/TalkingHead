import pyaudio
import wave

FORMAT = pyaudio.paInt16

CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 1

# start Recording

j = 1

while True:

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print "recording..."

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "finished recording"

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    file = open("RawFilesInRealTime/" + str(j) + ".raw", "wb")
    file.write(b''.join(frames))
    file.close()

    j = j + 1