from pydub import AudioSegment
from pydub.playback import play

import sys
import pyaudio
import wave
import argparse

#############################################
# VARIABLES
#############################################
chunk = 1024 #number of samples
FORMAT = pyaudio.paInt16
channels = 1 # 1:Mono, 2:Stereo
sample_rate = 44100 # Samples per second
number_of_seconds_recording = 2
##############################################

def test_sound(filename):
    sound = ""
    if filename.endswith(".mp3"):
        sound = AudioSegment.from_mp3(filename)
    elif filename.endswith(".wav"):
        sound = AudioSegment.from_wav(filename)
    else:
        print("Not mp3 or wav file")
    play(sound)

def record_sound(name_of_file):

    filename = name_of_file
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=channels, rate=sample_rate,
            input=True, output=True, frames_per_buffer=chunk)
    frames = []

    print("Recording sound...")

    for i in range(int(44100 / chunk *number_of_seconds_recording)):
        data = stream.read(chunk)

        # Simulatnously play the sound recorded 
        # stream.write(data)
        
        frames.append(data)

    print("Finished recording...")

    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()

def _command_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("--rec", default=False, action='store_true', help="If you want to record a new sound")
    parser.add_argument("--save", nargs='?', default="sound.wav",help='Filename for new record file')
    parser.add_argument("--load", nargs='?', default=None, help='Sound file to test')

    command_line_args = parser.parse_args()
    return command_line_args
if __name__ == "__main__":
    command_line_args = _command_arguments()
    
    if command_line_args.rec is True:
        print("Recording new sound, saving as: {}".format(command_line_args.save))
        record_sound(command_line_args.save)
    elif command_line_args.load is not None:
        test_sound(command_line_args.load)
    else:
        sys.exit(0)

