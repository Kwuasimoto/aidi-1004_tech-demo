# Local Speech-to-text translation using near state-of-the-art whisper-large-v3 from OpenAI.

import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


class SpeechToText:
    _device = "cuda:0" if torch.cuda.is_available() else "cpu"
    _torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    _model_id = "openai/whisper-large-v3"
    _model = AutoModelForSpeechSeq2Seq.from_pretrained(
        _model_id,
        torch_dtype=_torch_dtype,
        low_cpu_mem_usage=True,
        use_safetensors=True,
    )
    _processor = AutoProcessor.from_pretrained(_model_id)

    _pipe = pipeline(
        "automatic-speech-recognition",
        model=_model,
        tokenizer=_processor.tokenizer,
        feature_extractor=_processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        return_timestamps=True,
        torch_dtype=_torch_dtype,
        device=_device,
    )

    def __init__(self):
        torch.device(self._device)
        self._model.to(self._device)
        print("Speech-to-text instantiated")

    def speech_to_text(self, filename):
        return self._pipe(filename)

    def translate(self, filename):
        return self._pipe(filename)
