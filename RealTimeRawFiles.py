import pyaudio
import wave
import threading
import RealTimePhonemeGeneration

FORMAT = pyaudio.paInt16

CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 0.4

# start Recording
def run(mouth):
    j = 1

    while j<=5:

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

        t1 = threading.Thread(target=RealTimePhonemeGeneration.break_phoneme("RawFilesInRealTime/" + str(j) + ".raw", mouth))
        t1.start()

        j = j + 1

