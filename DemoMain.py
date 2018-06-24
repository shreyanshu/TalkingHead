import RawToPhoneme
import VedioFromImages
#

def run():
    phonemelist = RawToPhoneme.phonemes()
    # print(phonemelist)
    VedioFromImages.makeFaceAnimation(phonemelist)

