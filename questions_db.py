
question_list = [
    "受困在荒島100天如果只能攜帶一個物品，那會是什麼？", 
    "今天是星期五晚上，你的休閒活動是什麼？", 
    "需要熬夜的時候，你會選擇靠什麼提神？",
    "如果把人生的轉折比作題目，你認為自己遇到的哪種題目更多？",
    "在路上遇到熟人，你更習慣哪種打招呼的方式？",
    "走在路上需要解渴，你會選擇？",
    "路邊長了一棵不知名的小樹，你希望這棵樹是？",
    "你的口頭禪是？",
    "你認為工作中最重要的是什麼？",
    "和好朋友約好見面，但他卻沒有出現，你的想法是？",
    "當你戀愛時，最在意的是什麼？",
    "如果你看到別人有麻煩時，你會？",
]

options_list = [
    ["打火機", "書本", "口糧", "小刀"],
    ["追劇", "健身", "打遊戲", "出門跑趴"],
    ["咖啡", "酒", "綠茶", "汽水"],
    ["選擇題", "填空題", "判斷題", "開放題"],
    ["相識一笑", "攀談兩句", "肢體接觸", "假裝沒看到"],
    ["冷水", "熱水", "含糖飲料", "無糖茶"],
    ["正開花的櫻花樹", "在結果的楊桃樹", "能遮陰的榕樹", "行道樹"],
    ["「我要堅定」", "「這是為了你」", "「總會有辦法的」", "「如果別人不喜歡該怎麼辦？」"],
    ["完美", "團隊合作", "自己的風格", "毅力"],
    ["絕對不會原諒你遲到了！", "擔心他是不是發生什麼事", "等待好無聊，自己找些有趣的事做", "擔心是不是自己做錯了什麼"],
    ["誠實", "同情心", "悸動的感覺", "安全感"],
    ["在正義感驅使下，必須要幫助他", "溫柔地緊抱他", "給他一個微笑", "假裝沒看到"],
]

scores_list = [
    [[2, 0, 3, 1, 0], [3, 1, 2, 0, 1], [1, 0, 1, 3, 3], [0, 3, 1, 2, 0]],
    [[2, 1, 0, 1, 2], [0, 3, 2, 3, 0], [0, 0, 1, 2, 3], [3, 0, 2, 0, 1]],
    [[1, 0, 3, 1, 0], [2, 1, 3, 0, 1], [2, 2, 0, 2, 0], [0, 0, 1, 0, 3]],
    [[1, 2, 0, 2, 0], [1, 1, 0, 1, 0], [1, 3, 0, 3, 0], [1, 1, 3, 0, 2]],
    [[1, 1, 0, 1, 0], [1, 3, 0, 3, 0], [1, 1, 3, 0, 2], [2, 1, 0, 0, 2]],
    [[0, 3, 1, 2, 0], [2, 0, 0, 1, 0], [0, 0, 1, 0, 3], [2, 2, 0, 2, 0]],
    [[1, 3, 0, 2, 0], [1, 0, 0, 1, 1], [3, 0, 0, 1, 0], [1, 1, 3, 0, 2]],
    [[1, 3, 0, 2, 0], [2, 1, 0, 2, 0], [1, 0, 3, 0, 3], [2, 2, 0, 2, 0]],
    [[2, 2, 0, 2, 0], [1, 3, 0, 2, 0], [1, 0, 3, 1, 3], [1, 3, 0, 2, 0]],
    [[1, 1, 0, 0, 2], [1, 3, 0, 2, 0], [1, 1, 3, 0, 2], [1, 3, 0, 2, 0]],
    [[1, 3, 0, 2, 0], [1, 3, 0, 2, 0], [1, 2, 1, 0, 2], [1, 3, 0, 2, 0]],
    [[2, 0, 0, 1, 0], [1, 1, 3, 0, 0], [1, 3, 1, 2, 0], [0, 0, 0, 0, 4]],
]

qnum = len(question_list)

horoscope_list1 =[
    "摩羯座",
    "水瓶座",
    "雙魚座",
    "牡羊座",
    "金牛座",
    "雙子座",
    "以上皆非"
]
horoscope_list2 =[
    "巨蟹座",
    "獅子座",
    "處女座",
    "天秤座",
    "天蠍座",
    "射手座",
]

zodiacSigns_convent = {
    '牡羊座':'Aries',
    '金牛座':'Taurus',
    '雙子座':'Gemini',
    '巨蟹座':'Cancer',
    '獅子座':'Leo',
    '處女座':'Virgo',
    '天秤座':'Libra',
    '天蠍座':'Scorpio',
    '射手座':'Sagittarius',
    '摩羯座':'Capricorn',
    '水瓶座':'Aquarius',
    '雙魚座':'Pisces'
}

mood_weather = {
    '晴': 5,
    '晴時多雲': 4,
    '陰': 3,
    '雨': 2,
    '打雷閃電': 1
}
