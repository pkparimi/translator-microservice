from deep_translator import GoogleTranslator
from deep_translator.detection import single_detection


class Translator:
    def __init__(self, text, target, source='auto') -> None:
        self.text = text
        self.target = target
        self.source = source
        self.langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)

    def get_text(self) -> str:
        """
        Returns the original text.
        """
        return self.text

    def get_target(self) -> str:
        """
        Returns the user-specified target language.
        """
        if self.target not in self.langs_dict.keys():
            return list(self.langs_dict.keys())[list(self.langs_dict.values()).index(self.target)]
        else:
            return self.target

    def get_source(self) -> str:
        """
        Returns the user-specified source language or 'auto' if unspecified.
        """
        if self.source != 'auto' and self.source not in self.langs_dict.keys():
            return list(self.langs_dict.keys())[list(self.langs_dict.values()).index(self.source)]
        else:
            return self.source

    def get_lang_codes(self) -> dict:
        """
        Returns a dictionary with all supported languages and their respective codes.
        """
        return self.langs_dict

    def detect_lang(self) -> str:
        """
        Returns the language detected in the source text passed to the Translator class.
        """
        lang_code = single_detection(self.text, api_key='9a84cb3518b95093f719b8bf4b46359c')
        lang = list(self.langs_dict.keys())[list(self.langs_dict.values()).index(lang_code)]
        return lang
    
    def detect_lang_code(self) -> str:
        """
        Returns the language code detected in the source text passed to the Translator class.
        """
        lang_code = single_detection(self.text, api_key='9a84cb3518b95093f719b8bf4b46359c')
        return lang_code

    def translate(self) -> str:
        """
        Translates the source text into the target language and returns the final translated text.
        """
        if self.source == 'auto':
            final_text = GoogleTranslator(self.detect_lang_code(), self.target).translate(self.text)
        else:
            final_text = GoogleTranslator(self.source, self.target).translate(self.text)
        return final_text


if __name__ == "__main__":
    # translator = Translator("Thanks for using my translator. This is a template message. Please see documentation for usage.", 'es')

    # print(translator.get_text())
    # print("Source language: " + translator.get_source())
    # print("Detected language: " + translator.detect_lang())
    # print("Target language: " + translator.get_target())
    # print("Translation: " + translator.translate())

    # print("Supported languages:")
    # langs = translator.get_lang_codes()
    # for lang in langs:
    #     print(lang + ": " + langs[lang])
    new = Translator("Hello", "es")
    this_is = new.translate()
    print(this_is)