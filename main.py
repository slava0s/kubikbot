from pyrogram import Client, filters
import random
import os

token = os.environ['BOT_TOKEN'] 
api_id = os.environ['API_ID'] 
api_hash =  os.environ['API_HASH'] 
buname = os.environ['BUNAME']
app = Client(buname, api_id=api_id, api_hash=api_hash, bot_token=token)

@app.on_message(filters.command(["кто?", "кто", "who?", "who"]))
def echo(client, message):
    ulist  = app.get_chat_members(message.chat.id)
    str_ulist =[]
    for user in ulist:
        if (not user.user.is_bot):
            str_ulist.append(user.user.username if user.user.username else "[{tuname}](tg://user?id={uid})".format(
                uid=user.user.id,
                tuname=user.user.first_name))
    message.reply_text("@{username}".format(username=random.choice(str_ulist)))

app.run()
