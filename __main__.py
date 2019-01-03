#!/usr/bin/env python
import argparse
import numpy   as     np
from   pathlib import Path
import sounddevice

parser = argparse.ArgumentParser(description='plays noise')
parser.add_argument('--color', default='pink',
                    help='choices: blue, brown, pink, violet, or white')
args = parser.parse_args()

sounddevice.default.samplerate = 16e3

export_path = Path(__file__).parent / 'export'
filename    = str(export_path / '{color}_noise.npy')
samples = np.load(filename.format(color=args.color))
try:
    sounddevice.play(samples, blocking=True, loop=True)
except KeyboardInterrupt:
    print()
