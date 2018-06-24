
from os import environ, path

from pocketsphinx.pocketsphinx import *
# from sphinxbase.sphinxbase import *

MODELDIR = "C:/Python27/Lib/site-packages/pocketsphinx/model"
DATADIR = "C:/Python27/Lib/site-packages/data"
SAMPLE_RATE = 16000
CHUNK_SIZE = 1024

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us'))
config.set_string('-allphone', path.join(MODELDIR, 'en-us-phone.lm.dmp'))
config.set_float('-lw', 2.0)
config.set_float('-beam', 1e-10)
config.set_float('-pbeam', 1e-10)

def phonemes():
  # Decode streaming data
  decoder = Decoder(config)

  decoder.start_utt()
  stream = open('classtest2.raw', 'rb')
  while True:
    buf = stream.read()
    if buf:
      decoder.process_raw(buf, False, False)
    else:
      break
  decoder.end_utt()

  print([seg.word for seg in decoder.seg()])

  return [seg.word for seg in decoder.seg()]

phonemes()
