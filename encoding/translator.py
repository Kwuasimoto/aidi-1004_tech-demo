# Uses https://github.com/xtekky/gpt4free to utilize gpt ChatCompletions.
import g4f


class Translator:
    _content = """
        Conditions: 
        
        [
            If translating jp: return informal hiragana,
        ]
        
        Only return the translation of the following text to {}:
    
        {}
    """

    def __init__(self) -> None:
        print("Translator instantiated")

    def translate(self, text, lang):
        content = self._content.format(lang, text)
        response = g4f.ChatCompletion.create(
            stream=False,
            model=g4f.models.gpt_35_turbo,
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
        )

        return response
