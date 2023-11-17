# Uses https://github.com/xtekky/gpt4free to utilize gpt ChatCompletions.
import g4f


class Translator:
    _content = """
        Conditions: 
        
        if translating jp: return informal hiragana
        
        Only return the translation of the following text to {}:
    
        {}
    """

    def __init__(self) -> None:
        print("Translator instantiated")

    def translate(self, text, lang):
        content = self._content.format(lang, text)
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            provider=g4f.Provider.FreeGpt,
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
        )

        return response

    def question(self, text):
        return g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            provider=g4f.Provider.ChatgptAi,
            messages=[{"role": "user", "content": text}],
        )


# class Translator:
#     _device = "cuda:0" if torch.cuda.is_available() else "cpu"
#     _torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

#     _model_ids = {
#         "en-jp": "Helsinki-NLP/opus-mt-en-jap",
#         "jp-en": "Helsinki-NLP/opus-mt-jap-en",
#     }

#     _models = {
#         "en-jp": MarianMTModel.from_pretrained(_model_ids["en-jp"]),
#         "jp-en": MarianMTModel.from_pretrained(_model_ids["jp-en"]),
#     }

#     _tokenizers = {
#         "en-jp": MarianTokenizer.from_pretrained(_model_ids["en-jp"]),
#         "jp-en": MarianTokenizer.from_pretrained(_model_ids["jp-en"]),
#     }

#     _pipes = {
#         "en-jp": pipeline(
#             "translation",
#             model=_models["en-jp"],
#             tokenizer=_tokenizers["en-jp"],
#             torch_dtype=_torch_dtype,
#             device=_device,
#         ),
#         "jp-en": pipeline(
#             "translation",
#             model=_models["en-jp"],
#             tokenizer=_tokenizers["en-jp"],
#             torch_dtype=_torch_dtype,
#             device=_device,
#         ),
#     }

#     def translate(self, xx, yy, text):
#         translator = self._pipes[f"{xx}-{yy}"]
#         print(translator(text))
