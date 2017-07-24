1. # Prepare for processing
## Get FFMPEG
* Download ffmpeg from [ffmpeg](http://ffmpeg.zeranoe.com/builds/), you should select `Static` linking and get a zip file.
* extract the zip file into `ffmpeg` folder, __so that there exists `ffmpeg/bin/ffmeg.exe`__.

## Get SOX
* Download `sox` from [SOund eXchange](https://sourceforge.net/projects/sox/files/sox/14.4.2/), you should get a zip file.
* extract zip file into the `sox` folder. __so that there exists `sox/sox.exe`__.


2. # Convert Audio files to uniform format: *.wav
`$ python ./convert_file.py  XX/YY/raw`


3. # Output Images 

## Convert wavfile to spectrogram 

`python wavfile2spectrum.py ./wavfile`

* put spectrograms into `images/spectrum/`

## Convert wavfile to waveform 

`$python wavfile2waveform.py ./wavfile`

* put waveforms into `images/waveform/`




