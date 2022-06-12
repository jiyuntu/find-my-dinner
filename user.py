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
    
    def update_scores(self, scores):
        for i in range(5):
            self.scores[i] += scores[i]

    def classify_personality(self):
        self.personality = self.scores.index(max(self.scores))
        self.personality_str = User.personality_descriptions[self.personality]
        return self.personality


