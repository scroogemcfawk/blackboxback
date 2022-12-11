from django.core.management.base import BaseCommand

import telebot
from blackboxback.management.bot_settings import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

commands = ["start", "help", "idea"]


@bot.message_handler(commands=commands)
def process_command_message(message):
    if message.text.strip() == "/help":
        bot.send_message(message.from_user.id, "/help - get this message\n/idea [tags] - get an idea")
    elif message.text.strip() == "/start":
        bot.send_message(message.from_user.id,
                         "Welcome! I can generate an idea for your startup. Try /help for more info")
    else:
        # TODO: paste get_idea() here
        args = message.text.split(" ")
        if args[0] == "/idea":
            bot.send_message(message.from_user.id, "Generating idea")
            bot.send_message(message.from_user.id, "Idea {}\n\nNumber of employees:{}\nInvestments:{}")
        else:
            bot.send_message(message.from_user.id, "Failed to parse command args")


@bot.message_handler(content_types=['text'])
def process_text_message(message):
    bot.send_message(message.from_user.id, text="Try /help for more info")


class Command(BaseCommand):
    help = 'Django Bot handler'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
