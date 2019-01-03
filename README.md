# Make Noise

Simple noise (audio) generation and playback in Python.

## Requires

Tested in Python 3.7, but probably works in 2.7 as well.

`numpy` is required for generating the sound files. `numpy` and `sounddevice` are required for playback.

## Install

```shell
git clone https://github.com/Terrabits/make-noise.git
cd make-noise
pip install -r requirements.txt
```

## Use

To create noise files in `export/`:

`python export.py`

To play noise:

`python . [color]`

Where color options are `white`, `pink`, `blue`, `brown`, `violet`.

The default color is `pink`.

## References

This project was based on the Github repo [scivision/soothing-sounds](https://github.com/scivision/soothing-sounds), adapted for my use case.
