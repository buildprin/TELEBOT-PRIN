import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Replace 'YOUR_BOT_TOKEN' with the token you get from BotFather
TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create the custom keyboard
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # Define the requested buttons
    btn_account = KeyboardButton('👨🏻‍💻 គណនី')
    btn_shop = KeyboardButton('🛍️ ហាងសេវា')
    btn_info = KeyboardButton('💬 អ្នកផ្ដល់ព័ត៌មាន')
    
    # Add buttons to the keyboard (row_width=2 puts two buttons on the first row)
    markup.add(btn_account, btn_shop)
    markup.add(btn_info)
    
    welcome_text = "សូមស្វាគមន៍! សូមជ្រើសរើសជម្រើសខាងក្រោម៖"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_menu_clicks(message):
    # Handle the specific button clicks
    if message.text == '👨🏻‍💻 គណនី':
        bot.reply_to(message, "អ្នកបានជ្រើសរើស៖ គណនី (Account)")
    elif message.text == '🛍️ ហាងសេវា':
        bot.reply_to(message, "អ្នកបានជ្រើសរើស៖ ហាងសេវា (Service Shop)")
    elif message.text == '💬 អ្នកផ្ដល់ព័ត៌មាន':
        bot.reply_to(message, "អ្នកបានជ្រើសរើស៖ អ្នកផ្ដល់ព័ត៌មាន (Information)")
    else:
        bot.reply_to(message, "សូមជ្រើសរើសប៊ូតុងដែលមានស្រាប់។")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
