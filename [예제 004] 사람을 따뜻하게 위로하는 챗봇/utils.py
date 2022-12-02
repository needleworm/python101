"""
2022. 05. 10. 
Byunghyun Ban

bhban@kakao.com
https://github.com/needleworm/python101
"""
import random


class Eliza:
    def __init__(self, reply_dict):
        self.reply_dict = reply_dict
        self.conjugation = {
            "are": "am",
            "were": "was",
            "i": "you",
            "i'm": "you are",
            "my": "your",
            "me": "you",
            "i've": "you've",
            "you": "i",
            "your": "my",
            "myself": "yourself",
            "yourself": "myself",
            "am": "are"
        }
        self.keyword_conjugations = {
            "": "",
            "mom": "family",
            "dad": "family",
            "brother": "family",
            "sister": "family",
            "husband": "family",
            "wife": "family",
            "mother": "family",
            "father": "family",
            "brothers": "family",
            "sisters": "family",
            "grandfather": "family",
            "grandmohter": "family",
            "friends": "friend",
            "pal": "friend",
            "mate": "friend",
            "buddy": "friend",
            "buddies": "friend",
            "dreams": "dream",
            "nightmare": "dream",
            "nightmares": "dream",
            "sleep": "dream",
            "loves": "love",
            "love": "love",
            "loved": "love",
            "affair": "love",
            "hates": "hate",
            "dislike": "hate",
            "scared": "fear",
            "afraid of": "fear",
            "scary": "fear",
            "hi": "hello",
            "greeting": "hello",
            "mad": "angry",
            "anger": "angry",
            "furious": "angry",
            "fury": "angry",
            "sorry": "sorry",
            "apology": "sorry",
            "sadness": "sad",
            "sorrow": "sad",
            "work": "job",
            "works": "job",
            "boss": "job",
            "jobs": "job",
            "depressed": "depression",
            "depression": "depression",
            "religion": "religion",
            "religious": "religion",
            "god": "religion",
            "church": "religion",
            "money": "money",
            "fund": "money",
            "investment": "money",
            "invest": "money",
            "invested": "money",
            "feel": "feel",
            "feeling": "feel",
            "feels": "feel",
            "felt": "feel",
            "name": "name",
            "names": "name",
            "named": "name",
            "i": "i",
            "my": "my",
            "me": "i",
            "they": "3_main",
            "them": "3_",
            "their": "3_own",
            "it": "3_main",
            "its": "3_own",
            "he": "3_main",
            "his": "3_own",
            "him": "3_",
            "she": "3_main",
            "her": "3_",
            "yes": "yes",
            "no": "no",
            "what": "wh_questions",
            "where": "wh_questions",
            "why": "wh_questions",
            "who": "wh_questions",
            "whom": "wh_questions",
            "which": "wh_questions",
            "how": "wh_questions",
            "when": "wh_questions",
            "can": "can",
            "want": "want",
            "wanted": "want",
            "wants": "want",
            "thinks": "think",
            "think": "think",
            "remember": "remember",
            "remembers": "remember"
        }
        self.chat_start()

    def chat_start(self):
        print("[System] q() or quit() to stop chatting.\n")
        print("ELIZA> Hi, I'm ELIZA. What's your problem?")

        last_input = ""
        while True:
            line = self.sanitize(input("> "))
            if not line:
                answer = random.choice(["Hello?", "Are you still there?", "I'm listening."])
                print("ELIZA> " + answer)
            if line in "q() quit() Q() Quit()":
                print("ELIZA> Bye!")
                print("[System] ELIZA has leaved.")
                break
            elif line == last_input:
                print("ELIZA> Please say something new.")
                continue
            else:
                last_input = line
                origin, answer = self.find_keyword(line)
                if answer.endswith("*"):
                    answer = answer[:-1]
                    res = line.split(origin)[1].strip().split(" ")
                    res2 = []
                    for el in res:
                        if el in self.conjugation.keys():
                            el = self.conjugation[el]
                        res2.append(el)
                    res = " ".join(res2)
                    answer = answer + res
                print("ELIZA> " + answer)

    def find_keyword(self, line):
        line = line.split(" ")
        for el in line:
            if el in self.keyword_conjugations.keys():
                answer = random.choice(self.reply_dict[self.keyword_conjugations[el]])
                if answer == "":
                    continue
                return el, answer

        return "", "Sorry, I don't understand."

    @staticmethod
    def sanitize(line):
        line = line.lower().strip()

        rpx = [
            '^', '[', ']', '(', ')', "'", '"', '-',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            ':', ';', '_', '+', '=', '&', '!', '.', ',', '?',
            '#', '$', '%', '*', '<', '>', '\\', '|', '`', '~'
        ]
        for el in rpx:
            line = line.replace(el, "")

        return line
