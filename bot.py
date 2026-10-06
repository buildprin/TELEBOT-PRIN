import telebot
import yt_dlp
import os

# បញ្ចូល API Token ដែលអ្នកទទួលបានពី @BotFather
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
bot = telebot.TeleBot(BOT_TOKEN)

# ឆ្លើយតបនៅពេលអ្នកប្រើប្រាស់វាយ /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "សួស្តី! សូមផ្ញើ Link វីដេអូ YouTube មកកាន់ខ្ញុំ ខ្ញុំនឹងទាញយកវាជូនអ្នក។")

# ទទួល Link ពីអ្នកប្រើប្រាស់ និងដំណើរការទាញយក
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    
    # ពិនិត្យមើលថាតើវាជា Link YouTube ដែរឬទេ
    if "youtube.com" not in url and "youtu.be" not in url:
        bot.reply_to(message, "សូមបញ្ជូនតែ Link របស់ YouTube ប៉ុណ្ណោះ!")
        return

    bot.reply_to(message, "ទិន្នន័យកំពុងដំណើរការ... សូមរង់ចាំបន្តិច!")

    # កំណត់ជម្រើសក្នុងការទាញយក (យកជាប្រភេទ MP4 និងកំណត់ទំហំឱ្យតូចជាង 50MB ដើម្បីអាចផ្ញើតាម Telegram បាន)
    ydl_opts = {
        'format': 'best[ext=mp4][filesize<50M]', 
        'outtmpl': 'video_%(id)s.%(ext)s',
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ទាញយកព័ត៌មាន និងទាញយកវីដេអូ
            info = ydl.extract_info(url, download=True)
            filename = f"video_{info['id']}.mp4"

        # ផ្ញើវីដេអូត្រឡប់ទៅកាន់អ្នកប្រើប្រាស់វិញ
        with open(filename, 'rb') as video:
            bot.send_video(message.chat.id, video, caption="ទាញយករួចរាល់ដោយជោគជ័យ!")
        
        # លុបវីដេអូចេញពីកុំព្យូទ័រ/Server វិញ ដើម្បីសន្សំទំហំផ្ទុក
        os.remove(filename)

    except Exception as e:
        bot.reply_to(message, "សុំទោស មានបញ្ហាក្នុងការទាញយក។ វីដេអូនេះអាចមានទំហំធំជាង 50MB ឬ Link មិនត្រឹមត្រូវ។")

print("Bot កំពុងដំណើរការ... ចុច Ctrl+C ដើម្បីបញ្ឈប់។")
bot.infinity_polling()
