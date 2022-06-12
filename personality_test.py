import random

from telegram import (
    Update,
)
from telegram.constants import ParseMode
from telegram.ext import (
    CallbackContext,
    ContextTypes,
)

import questions_db as qdb

from user import User

# current_num_questions = {}
users = {}
MAX_QUESTIONS = 1

async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id=None) -> None:
    """Sends a predefined poll"""
    # identify which user is being processed
    chat_id = update.effective_chat.id if update else chat_id
    if chat_id not in users:
        users[chat_id] = User(qdb.qnum, chat_id)
    
    # do personality test
    if users[chat_id].personality < 0:
        # obtain question id
        question_id = users[chat_id].qid_sequence[users[chat_id].qcount]
        users[chat_id].qcount += 1
        # construct message
        message = await context.bot.send_poll(
            chat_id,
            qdb.question_list[question_id],
            qdb.options_list[question_id],
            is_anonymous=False,
        )
        # Save some info about the poll the bot_data for later use in receive_poll_answer
        payload = {
            message.poll.id: {
                "options": qdb.options_list[question_id],
                "scores" : qdb.scores_list[question_id],
                "message_id": message.message_id,
                "chat_id": chat_id,
            }
        }
        
    # ask for the horoscope
    else:
        horoscope_list = qdb.horoscope_list1 if users[chat_id].horoscope==-1 else qdb.horoscope_list2
        message = await context.bot.send_poll(
            chat_id,
            "請問您的星座是？",
            horoscope_list,
            is_anonymous=False,
        )
        payload = {
            message.poll.id: {
                "options": horoscope_list,
                "message_id": message.message_id,
                "chat_id": chat_id,
            }
        }
    context.bot_data.update(payload)


async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    # obatain the option choosed by the user
    answer = update.poll_answer
    answered_poll = context.bot_data[answer.poll_id]
    chat_id = answered_poll["chat_id"]
    message_id = answered_poll["message_id"]
    try:
        options = answered_poll["options"]
    except KeyError:
        # this means this poll answer update is from an old poll, we can't do our answering then
        return
    selected_options = answer.option_ids
    answer_string = options[selected_options[0]]
    # do personality test
    if users[chat_id].personality < 0:
        # show the user their response
        await context.bot.send_message(
            chat_id,
            f"{update.effective_user.mention_html()} 回答：{answer_string}。",
            parse_mode=ParseMode.HTML,
        )
        # update user's scores
        scores = answered_poll["scores"][selected_options[0]]
        users[chat_id].update_scores(scores)
    # ask for the horoscope
    else:
        await context.bot.send_message(
            chat_id,
            f"{update.effective_user.mention_html()} 回答：{answer_string}。",
            parse_mode=ParseMode.HTML,
        )
        user_horoscope = users[chat_id].update_horoscope(answer_string, selected_options[0])
        print(user_horoscope)
    # show next poll (or stop)
    await context.bot.stop_poll(chat_id, message_id)
    if users[chat_id].qcount < MAX_QUESTIONS:
        await poll(None, context, chat_id)
    elif users[chat_id].personality < 0:
        # end personality test
        # obtain the calculated personality
        personality = users[chat_id].classify_personality()
        # show the user their personality type
        await context.bot.send_message(
            chat_id,
            f"{update.effective_user.mention_html()}，心理測驗結果出爐！\n你是「{users[chat_id].personality_str}」！",
            parse_mode=ParseMode.HTML,
        )
        # ask for the horoscope
        await poll(None, context, chat_id)
    elif users[chat_id].horoscope == -2:
        # ask for the horoscope AGAIN
        await poll(None, context, chat_id)
    else:
        await make_recommendation(update, context, chat_id)
        del users[chat_id]

async def make_recommendation(update: Update, context: ContextTypes.DEFAULT_TYPE, chat_id=None) -> None:
    # TODO : using the weather and horoscope,
    # determine the best food to recommend for the user's personality type
    food_str = "土" # to replace
    # show our recommendation
    await context.bot.send_message(
        chat_id,
        f"我覺得你今天適合吃{food_str}！", # maybe change to a better sentence
        parse_mode=ParseMode.HTML,
    )
