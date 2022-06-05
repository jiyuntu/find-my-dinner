import random

from telegram import (
    Update,
)
from telegram.constants import ParseMode
from telegram.ext import (
    CallbackContext,
)

questions = ["請選一個顏色", "當收到禮物時，你的反應是？"]
options = [
    ["紅色", "藍色", "黃色", "白色"],
    ["開心收下，並感謝對方", "靦腆接受，並輕輕放下禮物", "馬上拆開，並給予評價"]
    ]
current_num_questions = {}
MAX_QUESTIONS = 5

async def poll(update: Update, context: CallbackContext.DEFAULT_TYPE, chat_id=None) -> None:
    """Sends a predefined poll"""
    question_id = random.randint(0, len(questions) - 1)
    option = options[question_id]
    chat_id = update.effective_chat.id if update else chat_id
    message = await context.bot.send_poll(
        chat_id,
        questions[question_id],
        option,
        is_anonymous=False,
    )
    if chat_id not in current_num_questions:
        current_num_questions[chat_id] = 1
    else:
        current_num_questions[chat_id] += 1
    # Save some info about the poll the bot_data for later use in receive_poll_answer
    payload = {
        message.poll.id: {
            "questions": option,
            "message_id": message.message_id,
            "chat_id": chat_id,
        }
    }
    context.bot_data.update(payload)


async def receive_poll_answer(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer
    answered_poll = context.bot_data[answer.poll_id]
    try:
        questions = answered_poll["questions"]
    # this means this poll answer update is from an old poll, we can't do our answering then
    except KeyError:
        return
    selected_options = answer.option_ids
    answer_string = questions[selected_options[0]]
    await context.bot.send_message(
        answered_poll["chat_id"],
        f"{update.effective_user.mention_html()} feels {answer_string}!",
        parse_mode=ParseMode.HTML,
    )
    await context.bot.stop_poll(answered_poll["chat_id"], answered_poll["message_id"])
    if current_num_questions[answered_poll["chat_id"]] < MAX_QUESTIONS:
        await poll(None, context, answered_poll["chat_id"])
    else:
        current_num_questions[answered_poll["chat_id"]] = 0