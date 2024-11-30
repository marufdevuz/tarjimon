from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

if __name__ == "__main__":
    text_to_translate = "Salom, dunyo!"
    translated_text = translate_text(text_to_translate, target_language='uz')
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {translated_text}")
