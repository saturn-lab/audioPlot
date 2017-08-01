# 1. Prepare for processing
## 1.1 get FFMPEG
* Download `ffmpeg` from [ffmpeg](http://ffmpeg.zeranoe.com/builds/), you should select `Static` linking and get a zip file.
* extract the zip file into `ffmpeg` folder, __so that there exists `ffmpeg/bin/ffmeg.exe`__.

## 1.2 get SOX
* Download `sox` from [SOund eXchange](https://sourceforge.net/projects/sox/files/sox/14.4.2/), you should get a zip file.
* extract zip file into the `sox` folder. __so that there exists `sox/sox.exe`__.


# 2. Uniforming Audio files with same `*.wav` format: 
`$ python ./convert_file.py  ./rawfile/`


# 3. Output spectrogram and waveform images 

## 3.1 Convert wavfiles to spectrogram 

`python wavfile2spectrum.py ./wavfile`

* put spectrograms into `images/spectrum/`

## 3.2 Convert wavfiles to waveform 

`$python wavfile2waveform.py ./wavfile`

* put waveforms into `images/waveform/`




