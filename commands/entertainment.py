from api import meme_api

def handle_meme(message, bot):
    chat_id = message.chat.id
    meme_url = meme_api.get_random_meme()
    bot.send_photo(chat_id, photo=meme_url)

def handle_doggo(message, bot):
    chat_id = message.chat.id
    doggo_url = meme_api.get_random_dog_image()
    bot.send_photo(chat_id, photo=doggo_url)
