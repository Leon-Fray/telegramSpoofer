# Telegram Image Spoofer Bot

A Telegram bot that processes images by applying random transformations to make them unique while maintaining quality.

## Features

- 🔄 **Random Horizontal Flip**: 40% chance of flipping the image horizontally
- 🔁 **Slight Rotation**: Randomly rotates images by 1-2 degrees
- 🗑️ **Metadata Removal**: Strips all EXIF data and metadata from images
- 🖼️ **High Quality Output**: Exports as optimized PNG format

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Leon-Fray/telegramSpoofer.git
   cd telegramSpoofer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**
   - Copy `.env.example` to `.env`
   - Get your bot token from [@BotFather](https://t.me/BotFather) on Telegram
   - Add your token to the `.env` file:
     ```
     TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
     ```

4. **Run the bot**
   ```bash
   python bot.py
   ```

## Usage

1. Start a chat with your bot on Telegram
2. Send any image to the bot
3. The bot will process the image and send back:
   - A confirmation message with processing details
   - The processed image as a PNG file

## How It Works

The bot applies the following transformations to each image:
- Converts the image to RGB format for PNG compatibility
- 40% probability of horizontal flip
- Rotates the image by 1-2 degrees (randomly clockwise or counterclockwise)
- Removes all metadata (EXIF, location, etc.)
- Saves as optimized PNG format

