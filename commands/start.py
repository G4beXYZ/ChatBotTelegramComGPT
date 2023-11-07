def handle_start(message, bot):
    chat_id = message.chat.id
    bot_name = bot.get_me().first_name
    response_message = f"Olá, {message.from_user.first_name}. Eu sou o {bot_name} 2.0, uma versão melhorada do meu antecessor! Aproveite!"
    bot.send_message(chat_id, response_message)
