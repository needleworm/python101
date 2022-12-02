import utils as U

""" 이 아래에 코딩하세요! """

# 챗봇이 인식할 키워드와 답변입니다.
# 추가하거나, 제거하거나, 문장을 수정해 보세요!
reply_dict = {
    # 인사 관련 토픽
    "hello": [
            "Hi! This is your chatbot friend, Eliza!",
            "Well, nice to see you!",
            "I hope you come to me more often!"
        ],
    # 가족 관련 토픽
    "family": [
            "Tell me more about your family.",
            "Hwo do you get along with your family?",
            "Do you often think about your family?"
        ],
    # 친구 관련 토픽
    "friend": [
            "Do your friends worry about you?",
            "Do you feel happy, when you're with them?",
            "What do you usually do when you meet up with friends?"
        ],
    # 꿈 관련 토픽
    "dream": [
            "What do you think about the dream?",
            "Who usually appears on your dream?",
            "What did you think about it when you were in the dream?"
        ],
    # 사랑 관련 토픽
    "love": [
            "Are in love with somebody?",
            "I think love is what you need.",
            "Do you love *"
        ],
    # 증오 관련 토픽
    "hate": [
            "Do you hate that so much?",
            "Why do you think you have to hate *",
            "I hove the hate turn into love and peace."
        ],
    # 두려움 관련 토픽
    "fear": [
            "Fear makes you unhappy.",
            "Everyone has fear. It's not a shame.",
            "Why are you frightened by *"
        ],
    # 슬픔 관련 토픽
    "sad": [
            "Sad, yes. That sounds so sad. I'm sorry.",
            "Well, I hope i can wipe the sadness a little.",
            "You are precious to me. Please don't be so sad."
        ],
    # 행복 관련 토픽
    "happy": [
            "Happiness! It's a magic chemical reaction on your nerves!",
            "It sounds great! I'm getting happy now too!",
            "Congratulation! It sounds amaging!"
        ],
    # 분노 관련 토픽
    "angry": [
            "Please calm down. I understand you. Cheer up.",
            "That sounds so bad. Are you OK?",
            "Do you still feel so angry?"
        ],
    # 사과 관련 토픽
    "sorry": [
            "Apology accepted. That's fine now.",
            "Good. I'm ok with that.",
            "Ok. I'm not get angry anymore."
        ],
    # 일 관련 토픽
    "work": [
            "I'm an AI. I don work. Haha!",
            "Chatting with my client is my work.",
            "I don't like work. Let's just play some game instead."
        ],
    # 직업 관련 토픽
    "job": [
            "Do you feel competent in your work?",
            "Does your job satisfy yourself?",
            "What is your relationship with your boss like?"
        ],
    # 우울함 관련 토픽
    "depression": [
            "What do you think about when you're alone?",
            "How long have you been?",
            "I hope I can give a little piece of peace."
        ],
    # 종교 관련 토픽
    "religion": [
            "Do you believe in God?",
            "Are you a religious person?",
            "Does your faith make you feel comfortable?"
        ],
    # 돈 관련 토픽
    "money": [
            "Does money makes you laugh and cry?",
            "How do you react to financial stresses?",
            "Well, a chatbot doesn't need money. So I can't understand it."
        ],
    # 기분 관련 토픽
    "feel": [
            "Tell me more about such feelings.",
            "Do you often feel *",
            "Do you enjoy feeling *"
        ],
    # 이름 관련 토픽
    "name": [
            "Well, actually name is not an important thing for a chatbot.",
            "I don't care about names. Go on.",
            "Does human consider name precious? A chatbot doesn't."
        ],
    # 원해
    "want": [
            "Do you want *",
            "I know that you want *",
            "Do you really want *"
        ],
    # 2인칭 발화 관련 토픽
    "you": [
            "Well, I want to discuss on you. Not me.",
            "A secret makes a woman woman.",
            "Oh, I *"
        ],
    # 2인칭 소유격 발화 관련 토픽
    "your": [
            "What about your own *",
            "Why are you concerned about my *",
            "Well, i don't like that so much."
        ],
    # 1인칭 발화 관련 토픽
    "i": [
            "Oh, you *",
            "Tell me more.",
            "That's interesting."
        ],
    # 1인칭 소유격 발화 관련 토픽
    "my": [
            "Tell me more about it.",
            "Well, do you care?",
            "So you are happy?"
        ],
    # 3인칭 주격 관련 토픽
    "3_main": [
            "",
            "",
            ""
        ],
    # 3인칭 소유격 관련 토픽
    "3_own": [
            "",
            "",
            ""
        ],
    # 3인칭 목적격 관련 토픽
    "3_": [
            "",
            "",
            ""
        ],
    # 답변(거부) 관련 토픽
    "no": [
            "",
            "",
            ""
        ],
    # 동의 관련 토픽
    "yes": [
            "",
            "",
            ""
        ],
    # 가능성(할 수 있음) 관련 토픽
    "can": [
            "Well, I just wanted to help you.",
            "",
            ""
        ],
    # 필요해
    "need": [
            "",
            "",
            ""
        ],
    # 생각 관련
    "think": [
            "",
            "",
            ""
        ],
    # 기억 관련
    "remember": [
            "",
            "",
            ""
        ],
    # 의문사 관련
    "wh_questions": [
            "",
            "",
            ""
        ]
}

""" 코딩 종료! """

eliza = U.Eliza(reply_dict)
