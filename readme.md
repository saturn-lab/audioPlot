# Step 1. Prepare for processing
## Step 1.1 get FFMPEG
* Download `ffmpeg` from [ffmpeg](http://ffmpeg.zeranoe.com/builds/), you should select `Static` linking and get a zip file.
* extract the zip file into `ffmpeg` folder, __so that there exists `ffmpeg/bin/ffmeg.exe`__.

## Step 1.2 get SOX
* Download `sox` from [SOund eXchange](https://sourceforge.net/projects/sox/files/sox/14.4.2/), you should get a zip file.
* extract zip file into the `sox` folder. __so that there exists `sox/sox.exe`__.

## Step 1.3 specify the path to ffmpeg and sox
* On MacOSX, you can substitude Step 1.1, 1.2 by `brew install ffmpeg sox`
* edit `user_config.py` and make sure the `FFMPEG_PATH` and `SOX_PATH` is correct.

# Step 2. Uniforming Audio files with same `*.wav` format: 

`python3 ./convert_file.py  ./rawfile/`

# Step 3. Output spectrogram and waveform images 

## Step 3.1 Convert wavfiles to spectrogram 

`python3 wavfile2spectrum.py ./wavfiles_dir/`

* put spectrograms into `images/spectrum/`

## Step 3.2 Convert wavfiles to waveform 

`python3 wavfile2waveform.py ./wavfiles_dir/`

* put waveforms into `images/waveform/`




