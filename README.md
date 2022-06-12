# Find My Dinner
## Prerequisites
1. ```pip install python-telegram-bot -U --pre```
2. Register a telegram account
3. Create your bot
   1. Talk to [BotFather](https://t.me/botfather)
   2. Use ```/newbot``` command to create new bot and get your token
   ![](https://i.imgur.com/jTyxNQ2.png)
4. Create your own API key for map service following the step [here](https://developers.google.com/maps/get-started)
5. In `./config.ini`, replace `your_token` and `your_api_key` with your owns (**without** quotation marks)
6. ```python3 main.py```, and you can talk to you bot on Telegram.

## `/findfood` command
- The command allow you to find food according to the bot's recommandation or directly search for the desired food
- For the related package installations, see the comments at the beginning of `./food_search.py`
- Send the command as following (it's suggested to input food_name using Taiwanese characters):
```
/findfood [food_name]
```
- The recommanded restaurants is sorted by distance, and only rating > 3.9 is considered. The bot recommands at most top three of them.
<br><img src="https://i.imgur.com/YaNiRGz.jpg" width="60%"/>
