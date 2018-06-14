import RealTimePhonemeGeneration


def run():
    i = 1
    while i <= 800:
        print(RealTimePhonemeGeneration.break_phoneme("RawFilesInRealTime/" + str(i) + ".raw"))
        i = i + 1