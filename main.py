from telebot import TeleBot
import config
import handlers

bot = TeleBot(config.TELEBOT_TOKEN)

if __name__ == '__main__':
    handlers.register_handlers(bot)
    bot.polling(none_stop=True)
