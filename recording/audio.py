## Uses sounddevice to record audio and save it to a input.wav file to be used by Whisper-v3

import keyboard
import sounddevice as sd
import pyaudio
import numpy as np
import wave

from scipy.io.wavfile import write, read


class Audio:
    _audio = None
    _buffer = 1024
    _channels: int = 1
    _device: str = ""
    _dtype = pyaudio.paInt16
    _duration: float = 10
    _filename: str = "input.wav"
    _format: str = "wav"
    _frames: list = []
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
            sound_file = wave.open(self._filename, "wb")
            sound_file.setnchannels(self._channels)
            sound_file.setsampwidth(self._audio.get_sample_size(pyaudio.paInt16))
            sound_file.setframerate(self._freq)
            sound_file.writeframes(b"".join(self._frames))
            sound_file.close()
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

    def huh(self):
        print("huh?")

    def record(self):
        print(f"Press R to start recording audio [ouptut={self._filename}]")
        keyboard.wait("R")
        self._audio = pyaudio.PyAudio()
        try:
            stream = self._audio.open(
                format=self._dtype,
                channels=self._channels,
                rate=self._freq,
                frames_per_buffer=self._buffer,
                input_device_index=self._input_device,
                input=True,
            )

            print("Press S to stop recording...")
            while not keyboard.is_pressed("S"):
                audio_data = stream.read(1024)
                self._frames.append(audio_data)

            stream.stop_stream()
            stream.close()
            self._audio.terminate()

            self.export()
            self._audio = None
        except Exception as e:
            print(e)
