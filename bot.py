import telebot
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ទាញយក Token ពី Railway Environment Variables
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    btn_account = KeyboardButton('👨🏻‍💻 គណនី')
    btn_shop = KeyboardButton('🛍️ ហាងសេវា')
    btn_info = KeyboardButton('💬 អ្នកផ្ដល់ព័ត៌មាន')
    
    markup.add(btn_account, btn_shop)
    markup.add(btn_info)
    
    welcome_text = "សូមស្វាគមន៍! សូមជ្រើសរើសជម្រើសខាងក្រោម៖"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_menu_clicks(message):
    if message.text == '👨🏻‍💻 គណនី':
        bot.reply_to(message, "អ្នកបានជ្រើសរើស៖ គណនី (Account)")
    elif message.text == '🛍️ ហាងសេវា':
        bot.reply_to(message, "អ្នកបានជ្រើសរើស៖ ហាងសេវា (Service Shop)")
    elif message.text == '💬 អ្នកផ្ដល់ព័ត៌មាន':
        bot.reply_to(message, "អ្នកបានជ្រើសរើស៖ អ្នកផ្ដល់ព័ត៌មាន (Information)")
    else:
        bot.reply_to(message, "សូមជ្រើសរើសប៊ូតុងដែលមានស្រាប់។")

if __name__ == "__main__":
    print("Bot is running on Railway...")
    bot.infinity_polling()
