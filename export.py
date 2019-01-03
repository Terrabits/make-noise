#!/usr/bin/env python
from   lib       import create_noise
from   lib.noise import colors
import numpy     as     np
from   pathlib   import Path

export_path = Path(__file__).parent / 'export'
export_path.mkdir(exist_ok=True)
filename = str(export_path / '{color}_noise.npy')

sample_rate_Hz = 16e3
seconds        = 60
for color in colors:
    samples = create_noise(color, sample_rate_Hz, seconds)
    np.save(filename.format(color=color), samples)
