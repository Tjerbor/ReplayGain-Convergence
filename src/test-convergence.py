import glob
import os
import subprocess
from pathlib import Path

def remove_wav(path):
    for wav in glob.glob(f'{path}/*.wav'):
        os.remove(wav)


def create_silence(length):
    samplerate = 44100
    subprocess.run(
        ['ffmpeg', '-f', 'lavfi', '-i', f'sine=frequency=4000:sample_rate={samplerate}', '-t', f'{length}',
         '-acodec', 'pcm_s16le', f'silence{float(length):.10f}.wav', '-y'])

def rsgain(path):
    subprocess.run(['rsgain','easy','-p','default','-m','MAX',f'{path}'])


def main():
    remove_wav(Path(__file__).parent)
    for i in range(390,410):
        create_silence(f'{float(i)/1000.0}')
    rsgain(Path(__file__).parent)


if __name__ == '__main__':
    main()
