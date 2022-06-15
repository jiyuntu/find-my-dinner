import random

foods = [
    ["刈包", "臭豆腐", "雞肉飯", "涼麵", "鴨肉羹", "鱔魚意麵", "肉圓", "蚵仔煎", "羊肉爐", "米粉"],
    ["蛋包飯", "咖哩", "炸豬排", "拉麵", "天婦羅", "牛丼", "壽司", "烏龍麵", "關東煮", "壽喜燒"],
    ["義大利麵", "牛排", "燉飯", "千層麵", "牛肉丸", "Taco", "德國豬腳", "捲餅", "西班牙烤飯", "法式雜菜褒"],
    ["Poke", "地瓜", "雞肉", "花椰菜飯", "鹹水雞", "沙拉", "水煮餐盒", "火鍋", "Subway", "生魚片"],
    ["麥當勞", "漢堡王", "摩斯漢堡", "肯德基", "必勝客", "達美樂", "拿坡里", "胖老爹", "起家雞", "Nene Chicken"]
]

# hot and rainy: 3
# hot and sunny: 2
# cold and rainy: 1
# cold and sunny: 0
food_weather = [
    [2, 2, 3, 3, 0, 1, 2, 2, 1, 3],
    [2, 3, 2, 1, 2, 2, 2, 1, 0, 0],
    [3, 2, 0, 1, 2, 2, 2, 2, 1, 1],
    [2, 1, 3, 2, 2, 2, 3, 0, 3, 2],
    [1, 2, 1, 2, 2, 1, 2, 1, 2, 1]
]

food_types = [ "台灣小吃", "日式料理", "異國料理", "健康餐", "速食" ]

def get_weather_type(t, h):
    if t > 22:
        return 3 if h>=50 else 2
    else:
        return 1 if h>=50 else 0

def get_food_recommendation(p:int, t:int, h:int)->str:
    weather_type = get_weather_type(t, h)
    food_list = []
    for i in range(10):
        if food_weather[p][i]==weather_type:
            food_list.append(foods[p][i])
    if food_list:
        return random.choice(food_list)
    return random.choice(foods[p])