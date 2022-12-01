import time

try:
    from gtts import gTTS
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'gtts'])
    try:
        from gtts import gTTS
    except ModuleNotFoundError:
        time.sleep(2)
        from gtts import gTTS


def say(text, filename, language="ko"):
    tts = gTTS(text=text, lang=language)
    tts.save(filename)
