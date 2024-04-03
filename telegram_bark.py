import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '1234567890:xxxxxxxxx'    # 1234567890:xxxxxxxxx为Telegram Bot的Token
ADMIN_ID = xxxxx    # xxxxx为管理员ID
BARK_BASE_URL = "https://api.day.app/xxxxx/TG有消息哦"    # xxxxx为bark的通知ID，最后的“TG有消息哦”可以自行修改
WHITELIST_FILE = 'whitelist.txt'    # whitelist.txt为白名单ID列表，只有在此白名单的用户可以发送通知
whitelist = set()

def load_whitelist():
    if os.path.exists(WHITELIST_FILE):
        with open(WHITELIST_FILE, 'r') as f:
            for line in f:
                whitelist.add(int(line.strip()))

def save_whitelist():
    with open(WHITELIST_FILE, 'w') as f:
        for item in whitelist:
            f.write(str(item) + '\n')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("欢迎使用Bark提醒小助手，本Bot可以发送即时通知")    # 此处内容可修改

def notifylite(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in whitelist:
        update.message.reply_text("你没有权限使用这个命令!")
        return

    content = " ".join(context.args) if context.args else "有消息哦"  # 此处“有消息哦”可以修改
    url = f"{BARK_BASE_URL}/{content}/"

    r = requests.get(url)
    if r.status_code == 200:
        update.message.reply_text("通知已发送!")
    else:
        update.message.reply_text("发送失败!")
        
def notify(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in whitelist:
        update.message.reply_text("你没有权限使用这个命令!")
        return

    content = " ".join(context.args) if context.args else "有消息哦"  # 此处“有消息哦”可以修改
    url = f"{BARK_BASE_URL}/{content}/?sound=typewriters"

    r = requests.get(url)
    if r.status_code == 200:
        update.message.reply_text("通知已发送!")
    else:
        update.message.reply_text("发送失败!")

def white(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_ID:
        update.message.reply_text("只有管理员可以使用此命令!")
        return

    args = context.args
    if not args:
        update.message.reply_text("请输入用户或群组ID!")
        return

    try:
        user_or_group_id = int(args[0])
        whitelist.add(user_or_group_id)
        save_whitelist()
        update.message.reply_text(f"ID {user_or_group_id} 已添加到白名单!")
    except ValueError:
        update.message.reply_text("无效的ID!")
        
def getid(update: Update, context: CallbackContext) -> None:
    chat_type = update.message.chat.type
    chat_id = update.message.chat.id

    if chat_type == "private":
        user_id = update.message.from_user.id
        update.message.reply_text(f"你的ID是: {user_id}")

    elif chat_type in ["group", "supergroup"]:
        if update.message.reply_to_message:  # Check if the command is a reply to another message
            replied_user_id = update.message.reply_to_message.from_user.id
            update.message.reply_text(f"用户的ID是: {replied_user_id}\n群组的ID是: {chat_id}")
        else:
            update.message.reply_text(f"群组的ID是: {chat_id}")

def main() -> None:
    load_whitelist()
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("notifylite", notifylite, pass_args=True))
    dp.add_handler(CommandHandler("notify", notify, pass_args=True))
    dp.add_handler(CommandHandler("white", white, pass_args=True))
    dp.add_handler(CommandHandler("getid", getid, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
