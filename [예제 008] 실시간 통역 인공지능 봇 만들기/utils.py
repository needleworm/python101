"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""
import time

try:
    from kakaotrans import Translator as T
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'kakaotrans'])
    try:
        from kakaotrans import Translator as T
    except ModuleNotFoundError:
        time.sleep(2)
        from kakaotrans import Translator as T


translator = T()


def en_to_kr(sentence):
    return translator.translate(sentence, src="en", tgt="kr")


def kr_to_en(sentence):
    return translator.translate(sentence, src="kr", tgt="en")
