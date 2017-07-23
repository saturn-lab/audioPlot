#!/opt/anaconda3/bin/python
# -*- coding:utf-8 -*-

import os
import glob
import sys

import matplotlib.pyplot as plt

from wavReader import readWav

def ConvertFile2Waveform(audio, dir_out):
  fname = os.path.basename(audio)
  
  rate, data =readWav(audio)
	
  fname = fname.split('.')[0]
  
  fname = os.path.join(dir_out, fname)
  
  print(fname)
  
  plt.plot(data)
  
  plt.savefig(fname + '.png')

  plt.close()
  
  return True
 
def ConvertAudioToWaveform(dir_in, dir_out=os.path.join('.', 'image', 'waveform')):
  if not os.path.exists(dir_in):
    raise(ValueError(dir_in + ' does not exist'))
	
  if not os.path.exists(dir_out):
    raise(ValueError(dir_out + ' does not exist'))
	
  audios = glob.glob(os.path.join(dir_in, '*.*'))
  
  print(audios)
  
  for audio in audios:
    ConvertFile2Waveform(audio, dir_out)
  return
  
if __name__ == '__main__':
  ConvertAudioToWaveform(sys.argv[1])