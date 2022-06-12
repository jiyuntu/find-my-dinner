import random
class User():
    # strings describing the 5 personalities
    personality_descriptions = [
        "在地知識分子",
        "義勇奉公的武士道精神",
        "異國風情的神祕女子",
        "健康至上的醫生",
        "愛吃炸雞的小孩"
    ]
    horoscope_list =[
        "摩羯座",
        "水瓶座",
        "雙魚座",
        "牡羊座",
        "金牛座",
        "雙子座",
        "巨蟹座",
        "獅子座",
        "處女座",
        "天秤座",
        "天蠍座",
        "射手座",
    ]
    def __init__(self, qnum, chat_id):
        # id of the chatroom
        self.chat_id = chat_id
        # get a random sequence of questions
        self.qcount = 0
        self.qid_sequence = list(range(qnum))
        random.shuffle(self.qid_sequence)
        # scores to classify the personality type of the user
        self.scores = [0, 0, 0, 0, 0]
        # personality : 0 1 2 3 4, init as -1
        self.personality = -1
        self.personality_str = "未知"
        # horoscope: 0 1 2 ... 11, init as -1, ask again: -2
        self.horoscope = -1
        self.horoscope_str = ""
    
    def update_scores(self, scores):
        for i in range(5):
            self.scores[i] += scores[i]

    def classify_personality(self):
        self.personality = self.scores.index(max(self.scores))
        self.personality_str = User.personality_descriptions[self.personality]
        return self.personality

    def update_horoscope(self, ans_str:str, opt_id:int)->str:
        if ans_str=="以上皆非":
            self.horoscope = -2
        elif self.horoscope == -2:
            self.horoscope = opt_id + 6
        else:
            self.horoscope = opt_id
        self.horoscope_str = ans_str
        return self.horoscope_str
