import RawToPhoneme
import VedioFromImages
#

def run(mouth):
    phonemelist = RawToPhoneme.phonemes()
    # print(phonemelist)
    VedioFromImages.makeFaceAnimation(phonemelist, mouth)


