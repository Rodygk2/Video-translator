from deep_translator import GoogleTranslator

def translate(text, from_lang):

    translated = GoogleTranslator(
        source=from_lang,
        target="fr"
    ).translate(text)

    return translated