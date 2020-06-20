import telebot
import os

# Get this from the botfather, then store it as an env variable called "Bot_API_Token."  
bot = telebot.TeleBot(os.environ['Bot_API_Token'])

# This should match what you gave the BotFather as the bot name
bot_name = "BOT NAME HERE"

# Channel ID should be in the format of "@channelName" - can be found in channel description. 
channel_id = "CHANNEL ID HERE"


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"Hey there! Send me a message and I'll forward it as an anonymous message to the {channel_id} channel!")

@bot.message_handler(commands=['help', 'SayHi'])
def forward_message(message):
	bot.send_message(channel_id, f"Howdy! I'm {bot_name}! Click my name and send me a private message and I'll forward it as an anonymous message to this channel! Don't abuse me please!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print(message.text)
	bot.send_message(channel_id, message.text)

def main():
	try: 
		bot.polling()   
	except Exception as e:
		print(e)
		main()


if __name__ == "__main__":
	main()
