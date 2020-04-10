from instabot import Bot
import os

bot = Bot()
bot.login(username="boringtestb", password="Wannabeonforbes98.")
# followers = bot.get_user_followers(bot.user_id)
bot.upload_photo(os.path.abspath('../AIs/Upload_test.jpg'),'Testing Map Upload via code...')