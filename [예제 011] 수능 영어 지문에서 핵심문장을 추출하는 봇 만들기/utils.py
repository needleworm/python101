"""
2022. 12. 01.
Byunghyun Ban
bhban@kakao.com
https://github.com/needleworm/python101
"""
import time

try:
    from summa import summarizer as S
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'summa'])
    try:
        from summa import summarizer as S
    except ModuleNotFoundError:
        time.sleep(2)
        from summa import summarizer as S


def extract(text, ratio=0.2):
    return S.summarize(text, ratio=ratio)
