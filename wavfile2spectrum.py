# -*- coding:utf-8 -*-
import os
import os.path as osp
import glob
import sys
from user_config import SOX_PATH

SOX_COMMAND = SOX_PATH + ' %s  -n rate 4k spectrogram -r -o  %s'

def ConvertFile2Spectrum(audio, dir_out):
  fname = osp.basename(audio)
  fname = fname.split('.')[0]
  fname = osp.join(dir_out, fname)
  os.system(SOX_COMMAND%(audio, fname + '.png'))
  return True
 
def ConvertAudioToSpectrum(dir_in, dir_out=osp.join('.', 'image', 'spectrum')):
  if not osp.exists(dir_in):
    raise(ValueError(dir_in + ' does not exist'))
  if not osp.exists(dir_out):
    raise(ValueError(dir_out + ' does not exist'))
	
  audios = glob.glob(osp.join(dir_in, '*.*'))
  for audio in audios:
    ConvertFile2Spectrum(audio, dir_out)
  return
  
if __name__ == '__main__':
  ConvertAudioToSpectrum(sys.argv[1])
