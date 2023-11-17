# Utilizes the Bark model from HuggingFace
import torch
import warnings

from transformers import AutoProcessor, AutoModel
from scipy.io.wavfile import write

warnings.filterwarnings(action="ignore", category=UserWarning)


class Synthesizer:
    _filename = "output.wav"
    _device = "cuda" if torch.cuda.is_available() else "cpu"
    _voices = {
        "en": "v2/en_speaker_1",
        "fr": "v2/fr_speaker_2",
        "jp": "v2/ja_speaker_3",
    }

    _model_id = "suno/bark"
    _model = AutoModel.from_pretrained(_model_id).to(_device)

    def __init__(self) -> None:
        print("Text-to-speech initialized")
        if self._device == "cuda":
            self._model = self._model.to_bettertransformer()
            self._model.enable_cpu_offload()

    def synthesize(self, lang, text):
        processor = AutoProcessor.from_pretrained(
            self._model_id, voice_preset=self._voices[lang]
        )
        inputs = processor(text=[text], return_tensors="pt").to(self._device)
        return self._model.generate(**inputs, do_sample=True, pad_token_id=1337)

    def write(self, audio_array):
        sample_rate = self._model.generation_config.sample_rate
        write(
            self._filename, rate=sample_rate, data=audio_array.cpu().numpy().squeeze()
        )
