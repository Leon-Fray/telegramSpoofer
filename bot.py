import os
import random
from io import BytesIO
from PIL import Image
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()

def process_image(image_bytes):
    # Load image
    img = Image.open(BytesIO(image_bytes))

    # Convert to RGB (ensures PNG compatibility)
    img = img.convert("RGB")

    # ---- 40% HORIZONTAL FLIP ----
    if random.random() < 0.40:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # ---- 1–2 DEGREE ROTATION ----
    angle = random.uniform(1, 2)
    if random.random() < 0.5:
        angle = -angle
    img = img.rotate(angle, expand=True)

    # ---- REMOVE METADATA + SAVE PNG ----
    output = BytesIO()
    img.save(output, format="PNG", optimize=True)
    output.seek(0)
    return output

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.photo[-1].get_file()
    file_bytes = await file.download_as_bytearray()

    processed = process_image(file_bytes)

    # Send confirmation message
    await update.message.reply_text(
        "✅ Processed 1 images!\n"
        "• 40% horizontal flip chance\n"
        "• 1–2° rotations\n"
        "• Metadata removed\n"
        "• Maximum quality PNG"
    )

    # Send modified image back
    await update.message.reply_document(processed, filename="processed.png")

def main():
    application = Application.builder().token("8465431068:AAHNWVf2hgiwpg-29eATGvezCTPpcPf8SHU").job_queue(None).build()

    application.add_handler(MessageHandler(filters.PHOTO, handle_image))

    application.run_polling()

if __name__ == "__main__":
    main()
