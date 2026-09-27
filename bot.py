import telebot

# আপনার বটের টোকেন
TOKEN = "8408785625:AAHF24bNlf2cEfRt6BHbmd6E2ViM8bAmdfo"
bot = telebot.TeleBot(TOKEN)

# প্রাইভেট চ্যানেলের আইডি
CHANNEL_ID = -1002780787299

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # স্টার্ট লিংকের সাথে কোনো আইডি (যেমন ?start=99) আছে কিনা চেক করা
    args = message.text.split()
    if len(args) > 1:
        post_id = args[1]
        try:
            # চ্যানেল থেকে নির্দিষ্ট মেসেজ ইউজারের ইনবক্সে কপি করে পাঠানো
            bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=int(post_id))
        except Exception as e:
            bot.reply_to(message, "দুঃখিত, ফাইলটি পাঠানো সম্ভব হচ্ছে না বা এটি ডিলিট হয়ে গেছে।")
    else:
        bot.reply_to(message, "স্বাগতম! দয়া করে সঠিক লিংক ব্যবহার করুন।")

bot.infinity_polling()
