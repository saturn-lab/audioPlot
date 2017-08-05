#!/opt/anaconda3/bin/python
# -*- coding:utf-8 -*-

import os
import glob
import sys

SOX_PATH=os.path.join('.', 'sox', 'sox')

SOX_COMMAND = SOX_PATH + ' %s  -n rate 4k spectrogram -r -o  %s'

def ConvertFile2Spectrum(audio, dir_out):
  fname = os.path.basename(audio)
  fname = fname.split('.')[0]
  fname = os.path.join(dir_out, fname)
  os.system(SOX_COMMAND%(audio, fname + '.png'))
  return True
 
def ConvertAudioToSpectrum(dir_in, dir_out=os.path.join('.', 'image', 'spectrum')):
  if not os.path.exists(dir_in):
    raise(ValueError(dir_in + ' does not exist'))
  if not os.path.exists(dir_out):
    raise(ValueError(dir_out + ' does not exist'))
	
  audios = glob.glob(os.path.join(dir_in, '*.*'))
  for audio in audios:
    ConvertFile2Spectrum(audio, dir_out)
  return
  
if __name__ == '__main__':
  ConvertAudioToSpectrum(sys.argv[1])