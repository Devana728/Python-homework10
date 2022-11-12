from pytube import YouTube
import telebot


bot = telebot.TeleBot('5391583782:AAHUdvRJJE-O5lkTwd5KVRqHOfVE7lH6yeo')
@bot.message_handler(commands = ['старт'])
def send_welcome1(message):
	bot.reply_to(message, "Введите ссылку на видео")
@bot.message_handler(func=lambda message: True)
def yt_download(message):
    chat_id = message.chat.id
    yt = YouTube(message.text)
    yt.streams.filter(res="360p").first().download(filename=f"{chat_id}.mp4")
    bot.send_video(chat_id, video=open(f"{chat_id}.mp4",'rb'), supports_streaming=True)
    print(yt.title)
bot.infinity_polling()

