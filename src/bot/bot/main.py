from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from django.conf import settings
import requests
import json
from django.utils import timezone


def run():
    bot.set_webhook(settings.HOST + '/bot/')


bot: Bot = Bot(token=settings.TOKEN)

dispatcher = Dispatcher(bot, None)


def get_channel_members(channel_username):
    url = f"https://api.telegram.org/bot{settings.TOKEN}/getChatMembersCount?chat_id=@{channel_username}"
    with requests.get(url) as f:
        resp = json.load(f)
    return int(resp['result'])



def channel_post(update: Update, context):
    channel_username = update.channel_post.chat.username


def get_comment_msg(message_id):
    pass


def group_post(update: Update, context):
    message_id = update.message.message_id
    forward_from_chat = update.message.forward_from_chat
    now = timezone.now()



def message(update: Update, context):
    channel_msg = update.channel_post
    if channel_msg:
        return channel_post(update, context)
    else:
        return group_post(update, context)


def help(update: Update, context):
    msg_txt = """
<b>Botdan foydalanish bo'yicha qo'llanma 🆘</b>
<i>
1️⃣ Kanalga admin qilish
2️⃣ Kanalga biriktirilgan guruhga admin qilish
3️⃣ Guruhni <code>ommaviy guruh</code> qilish
4️⃣ Kanal va guruh linklarini pr.sport.uz tizimiga kiritish
</i>
"""
    update.message.reply_html(msg_txt)
    return True


all_handler = MessageHandler(Filters.all, message)
help_handler = CommandHandler('help', help)

dispatcher.add_handler(help_handler)
dispatcher.add_handler(all_handler)
