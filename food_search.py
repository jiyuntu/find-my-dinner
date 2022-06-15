import random
import geocoder		# pip install geocoder
import googlemaps   # pip install -U googlemaps
import configparser # pip install configparser
import requests     # pip install requests
import random
import urllib.parse # pip install urllib3

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.constants import ParseMode
from telegram.ext import (
    CallbackContext,
    ContextTypes,
)

# Load data from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Stickers to be sent in response to /findfood command
stickers = {'failed':
                ['CAACAgUAAxkBAAEE-E5ipMqPiMbGxmSsy-b1Ect1uAIo0QACRwIAAhQUsFcE-Bt61_JuxyQE',
                'CAACAgUAAxkBAAEE-FJipMqYfOpcUs1Kk3q2fzWuFkXARgACtwEAAufEuVdXA_3ZaD7qxCQE',
                'CAACAgUAAxkBAAEE-FRipMqaJkIeejP_KZ-QrU0OemozGwAC_AEAAreZsFeu0J-vq23RGCQE',
                'CAACAgEAAxkBAAEE-FZipMqoRlQH7FDKSKC_h7RRYDwS8QACTwQAAvoPCRTuQkYVX7Zo3yQE',
                'CAACAgEAAxkBAAEE-FhipMq1SJ1pSxDymDvdBFtcsavYKQACXgQAAvoPCRSE5NfsQLDwjSQE',
                'CAACAgUAAxkBAAEE-FpipMrXp4sHgdw5DhCzaF5uaRN8eAACbAIAAhN9uFeV0GBwNBjRBSQE'],
            'success':
                ['CAACAgEAAxkBAAEE-GlipNR0U_EJ3RJW82V4KmAKhQyhNgACYAQAAvoPCRS3EKMeok6pUSQE',
                'CAACAgEAAxkBAAEE-GtipNSGFPrW2amDhEL5oDMMvAoGpAACUQQAAvoPCRRuf5uP9vAS6CQE',
                'CAACAgEAAxkBAAEE-G1ipNSNHXZkTr_xMMlpGk6q13H0ygACSwQAAvoPCRSUBOKW89bAIiQE',
                'CAACAgUAAxkBAAEE-G9ipNSavZUvY8-n_SwTLTkWWOGS-gACRgEAAkU_uVdP9knYl9iqyCQE',
                'CAACAgIAAxkBAAEE-HVipNUGNBK7tctS7O46q3k6XmczdQACExUAAujW4hIHkK9B2skKGSQE',
                'CAACAgIAAxkBAAEE-HdipNUi2CKQop-3ajLM5aDJJJvCDQACHRUAAujW4hKrQdlNbs1rDyQE',
                'CAACAgIAAxkBAAEE-HlipNUmR05RbaT-_qE22q_cj5ulWAACEhUAAujW4hJOATSdWx1yKCQE']
            }


def decide_sticker(status: str):
    index = random.randint(0, len(stickers[status]) - 1)
    return stickers[status][index]

async def findfood_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id=None) -> None:
    """Sends the searched recommended list"""
    chat_id = update.effective_chat.id if update else chat_id
    
    if len(context.args) != 1:
        await update.message.reply_text("抱歉，請在 /findfood 後輸入欲查詢的美食名稱... <(_ _)>")
    else:
        gmaps = googlemaps.Client(key=config['GOOGLEMAP']['API_KEY'])
        usr_loc = geocoder.ip('me').latlng
        nearby_search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&types=restaurant&keyword={}&language=zh-TW&rankby=distance&key={}'.format(usr_loc[0], usr_loc[1], context.args[0], config['GOOGLEMAP']['API_KEY'])
        raw_result = requests.get(nearby_search_url).json()
        raw_restaurants = raw_result['results']
        
        restaurants = []
        for i in range(len(raw_restaurants)):
            if raw_restaurants[i].get('rating') == None or raw_restaurants[i].get('vicinity') == None or raw_restaurants[i].get('name') == None or raw_restaurants[i].get('place_id') == None:
                continue
            if raw_restaurants[i]['rating'] > 3.9:
                    restaurants.append(raw_restaurants[i])
            
        if len(restaurants) == 0:
            await update.message.reply_text("抱歉，沒有查詢到符合的餐廳... orz")
            sticker_id = decide_sticker('failed')
            await context.bot.send_sticker(chat_id, sticker_id)
        else:
            await update.message.reply_text("查詢到了美味的食物！\n以下列出幾個附近的好評餐廳～")
            sticker_id = decide_sticker('success')
            await context.bot.send_sticker(chat_id, sticker_id)
            
            n = 3 if len(restaurants) >= 3 else len(restaurants)
            selected_restaurants = restaurants[0:n]
            
            for res in selected_restaurants:
                rating = res['rating']
                address = res['vicinity']
                name = res['name']
                place_id = res['place_id']
                details = """<b>{}</b>
Google Map 評分：{}
地址：{}""".format(name, rating, address)
                
                # thumbnail = res.get('photos')
                # thumb_ref = thumbnail[0]['photo_reference']
                # thumb_wid = thumbnail[0]['width']
                # thumb_url = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth={}&photo_reference={}&key={}'.format(thumb_wid, thumb_ref, config['GOOGLEMAP']['API_KEY'])
                
                encoded_query = urllib.parse.quote_plus(name)
                map_url = 'https://www.google.com/maps/search/?api=1&query={}&query_place_id={}'.format(encoded_query, place_id)
                keyboard = [[InlineKeyboardButton("查看地圖", url=map_url)]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await context.bot.send_message(chat_id, details, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
