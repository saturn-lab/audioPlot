# -*- coding:utf-8 -*-

import os
import os.path as osp
import glob
import sys
import numpy as np
import matplotlib.pyplot as plt

from wavReader import readWav

def ConvertFile2Waveform(audio, dir_out):
    fname = osp.basename(audio)

    rate, data = readWav(audio)

    fname = fname.split('.')[0]

    fname = osp.join(dir_out, fname)

    print(fname)

    plt.figure()
    plt.plot(data)
    plt.savefig(fname + '.png')
    plt.close()

    return True


def ConvertAudioToWaveform(dir_in, dir_out=osp.join('.', 'image', 'waveform')):
    if not osp.exists(dir_in):
        raise(ValueError(dir_in + ' does not exist'))

    if not osp.exists(dir_out):
        raise(ValueError(dir_out + ' does not exist'))

    audios = glob.glob(osp.join(dir_in, '*.*'))

    print(audios)

    for audio in audios:
        ConvertFile2Waveform(audio, dir_out)
    return


if __name__ == '__main__':
    ConvertAudioToWaveform(sys.argv[1])
