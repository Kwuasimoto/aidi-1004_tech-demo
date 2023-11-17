## Uses sounddevice to record audio and save it to a input.wav file to be used by Whisper-v3

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write, read


class Audio:
    _channels: int = 2
    _device: str = ""
    _duration: float = 5
    _filename: str = "input.wav"
    _format: str = "wav"
    _freq: int = 44100
    _input_device: int = 1
    _recording = np.ndarray[np.float64]

    def __init__(self):
        print("Audio instantiated")

    def set_channels(self, channels: int = 2):
        self._channels = channels

    def set_duration(self, duration: float):
        self._duration = duration

    def filename(self):
        return self._filename

    def set_filename(self, filename: str = "input.wav"):
        self._filename = filename

    def set_format(self, format: str = "wav"):
        self._format = format

    def set_freq(self, freq: int):
        self._freq = freq

    def set_input_device(self):
        self.list_devices()
        print("Please select an audio device by index [0-n]: ")
        index = int(input())
        self._input_device = index

    def export(self):
        try:
            write(self._filename, self._freq, self._recording)
        except Exception as e:
            print(e)

    def list_devices(self, kind="input"):
        devices = sd.query_devices()
        print("Available input devices:")
        for i, device in enumerate(devices):
            print(f"{i} - {device['name']}")

    def load(self, filename=None):
        if filename == None:
            filename = self._filename
        try:
            return read(self._filename)
        except Exception as e:
            print(e)

    def record(self):
        try:
            # print(sd.default.device)
            self._recording = sd.rec(
                int(self._duration * self._freq),
                samplerate=self._freq,
                channels=self._channels,
                device=self._input_device,
            )
            sd.wait()
        except Exception as e:
            print(e)
