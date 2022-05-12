"""
2022. 05. 10. 
Byunghyun Ban

bhban@kakao.com
https://github.com/needleworm/python101
"""

class Eliza:
    def __init__(self, replies):
        self.replis = replies
        self.conjugation = {
            "are": "am",
            "were": "was",
            "I": "you",
            "I'm": "you are",
            "my": "your",
            "me": "you",
            "I've": "you've",
            "you": "I",
            "your": "my",
            "myself": "yourself",
            "yourself": "myself",
            "am": "are"
        }


