# Models from g4f seem to work and not work at different times, this file is meant for testing the translator providers.

import os
from recording import Audio
from encoding import Translator, Transcriber, Synthesizer

os.environ["TRANSFORMERS_CACHE"] = "./.tech_demo/cache"

audio = Audio()
transcriber = Transcriber()
translator = Translator()
synthesizer = Synthesizer()


if __name__ == "__main__":
    to_lang = "fr"
    # text = transcriber.transcribe(audio.filename())["text"]
    # print(f"Text from audio: [{text}]")

    translated = translator.translate(to_lang, "Hello my name is Thomas")

    for line in translated:
        print(line, flush=True, end="")

    # print(translator.question("Hello ChatGPT are you available?"))

    # print(f"Translated to {to_lang}: [{translated}]")

    # print("Synthesizing to audio, this takes a moment...")
    # synthesized = synthesizer.synthesize(to_lang, translated)
    # print("Synthesizing finished!")

    # synthesizer.write(synthesized)
    # print(f"Wrote translation to output.wav!")
    # print("Pipeline finished.")
