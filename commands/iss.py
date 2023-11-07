from api import space_api

def handle_iss(message, bot):
    chat_id = message.chat.id
    iss_info = space_api.get_iss_location()
    if iss_info:
        # Send ISS information to the user using bot.send_message
        pass
    else:
        bot.send_message(chat_id, "Não foi possível obter informações da ISS no momento.")
