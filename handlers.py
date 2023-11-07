from commands import start, iss, entertainment

def register_handlers(bot):
    # Start command
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        start.handle_start(message, bot)

    # ISS command
    @bot.message_handler(commands=['iss'])
    def iss_handler(message):
        iss.handle_iss(message, bot)

    # Meme command
    @bot.message_handler(commands=['meme'])
    def meme_handler(message):
        entertainment.handle_meme(message, bot)

    # Doggo command
    @bot.message_handler(commands=['doggo'])
    def doggo_handler(message):
        entertainment.handle_doggo(message, bot)

    # Add more handlers for other commands as needed
