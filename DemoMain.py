import RawToPhoneme
import VedioFromImages
#
phonemelist = RawToPhoneme.phonemes()
# print(phonemelist)
VedioFromImages.makeFaceAnimation(phonemelist)

