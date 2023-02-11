import pyrogram
from main import app
from pyrogram import Client, filters


@Client.on_message(filters.command("purge"))
def purge(client, message):
    if message.reply_to_message:
        client.delete_messages(message.chat.id, message.reply_to_message.message_id)
        client.delete_messages(message.chat.id, message.message_id)
    else:
        client.delete_messages(message.chat.id, message.message_id)
