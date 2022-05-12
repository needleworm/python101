import utils as U


""" 이 아래에 코딩하세요! """

# 챗봇이 인식할 키워드와 답변입니다.
# 추가하거나, 제거하거나, 문장을 수정해 보세요!
reply_dict = {
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
            "Love is beautiful!"
        ],
    # 증오 관련 토픽
    "hate": [
            "Do you hate that so much?",
            "Why do you think you have to hate that?",
            "I hove the hate turn into love and peace."
        ],
    # 두려움 관련 토픽
    "fear": [
            "Fear makes you unhappy.",
            "Everyone has fear. It's not a shame.",
            "I believe you are more than the fear!"
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
            "",
            "",
            ""
        ],
    # 학업 관련 토픽
    "study": [
            "",
            "",
            ""
        ],
    # 우울함 관련 토픽
    "depression": [
            "",
            "",
            ""
        ],
    # 용기 관련 토픽
    "courage": [
            "",
            "",
            ""
        ],
    # 종교 관련 토픽
    "religion": [
            "",
            "",
            ""
        ],
    # 인간관계 관련 토픽
    "relationship": [
            "",
            "",
            ""
        ],
    # 돈 관련 토픽
    "money": [
            "",
            "",
            ""
        ],
    # 기분 관련 토픽
    "feel": [
            "",
            "",
            ""
        ],
    # 인사 관련 토픽
    "hello": [
            "",
            "",
            ""
        ],
    # 이름 관련 토픽
    "name": [
            "",
            "",
            ""
        ],
    # 2인칭 발화 관련 토픽
    "you": [
            "",
            "",
            ""
        ],
    # 2인칭 소유격 발화 관련 토픽
    "your": [
            "",
            "",
            ""
        ],
    # 1인칭 발화 관련 토픽
    "i": [
            "",
            "",
            ""
        ],
    # 1인칭 소유격 발화 관련 토픽
    "my": [
            "",
            "",
            ""
        ],
    # 3인칭 관련 토픽
    "they": [
            "",
            "",
            ""
        ],
    # 3인칭 소유격 관련 토픽
    "their": [
            "",
            "",
            ""
        ],
    # 3인칭 관련 관련 토픽
    "it": [
            "",
            "",
            ""
        ],
    # 3인칭 소유격 관련 관련 토픽
    "its": [
            "",
            "",
            ""
        ],
    # 3인칭 남성 관련 관련 토픽
    "he": [
            "",
            "",
            ""
        ],
    # 3인칭 남성 소유격 관련 관련 토픽
    "his": [
            "",
            "",
            ""
        ],
    # 3인칭 여성 관련 관련 토픽
    "she": [
            "",
            "",
            ""
        ],
    # 3인칭 여성 소유격 관련 관련 토픽
    "her": [
            "",
            "",
            ""
        ],
    # 답변(승락) 관련 토픽
    "yes": [
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
    # 의문사 관련 토픽
    "wh_questions": [
            "",
            "",
            ""
        ],
    # 1인칭 가능성 관련 토픽
    "can i": [
            "",
            "",
            ""
        ],
    # 2인칭 가능성 관련 토픽
    "can you": [
            "",
            "",
            ""
        ],
    # 1인칭 가능성 부정 관련 토픽
    "i can't": [
            "",
            "",
            ""
        ],
    # 2인칭 가능성 부정관련 토픽
    "you can't": [
            "",
            "",
            ""
        ],
    # 1인칭 be동사 관련 토픽
    "i am": [
            "",
            "",
            ""
        ],
    # 2인칭 be동사 관련 토픽
    "you are": [
            "",
            "",
            ""
        ],
    # 1인칭 부정동사 관련 토픽
    "i don't": [
            "",
            "",
            ""
        ],
    # 2인칭 부정동사 관련 토픽
    "you don't": [
            "",
            "",
            ""
        ],
    # 3인칭 부정동사 관련 토픽
    "they don't": [
            "",
            "",
            ""
        ],
    # 제안 관련
    "why don't you": [
            "",
            "",
            ""
        ],
    # 1인칭 be동사 질문 관련
    "am i": [
            "",
            "",
            ""
        ],
    # 2인칭 be동사 질문 관련
    "are you": [
            "",
            "",
            ""
        ],
    # 원해
    "want": [
            "",
            "",
            ""
        ],
    # 필요해
    "need": [
            "",
            "",
            ""
        ],
    # 이유 관련
    "because": [
            "",
            "",
            ""
        ],
    # 추측 관련
    "maybe": [
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
        ]
}

""" 코딩 종료! """

eliza = U.Eliza(reply_dict)
