import torch
import torchaudio

import time
from typing import List

import IPython
import matplotlib.pyplot as plt
from torchaudio.models.decoder import ctc_decoder
from torchaudio.utils import _download_asset as download_asset

bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_10M
acoustic_model = bundle.get_model()
speech_file = "male.wav"

IPython.display.Audio(speech_file)