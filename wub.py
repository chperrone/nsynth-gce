import os
import numpy as np
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen

fname = 'wub2.mp3'
sr = 16000
audio = utils.load_audio(fname, sample_length=40000, sr=sr)
sample_length = audio.shape[0]
print('{} samples, {} seconds'.format(sample_length, sample_length / float(sr)))

encoding = fastgen.encode(audio, os.path.abspath('model.ckpt-200000'), sample_length)
print(encoding.shape)
np.save(fname + '.npy', encoding)

fastgen.synthesize(encoding, save_paths=['gen_' + fname], samples_per_save=sample_length)

sr = 16000
synthesis = utils.load_audio('gen_' + fname, sample_length=sample_length, sr=sr)

print('Magenta Test')