from instabot import Bot
import os

#from TwitterAPI import TwitterAPI


def uploadPicToInstagram(path, caption):
    bot = Bot()
    bot.login(username=YOUR_USERNAME, password=YOUR_PASSWORD)
    # followers = bot.get_user_followers(bot.user_id)

    bot.upload_photo(os.path.abspath(path), caption)



#def uploadPicToTwitter(path, caption):
 #   CONSUMER_KEY = ''
  #  CONSUMER_SECRET = ''
   # ACCESS_TOKEN_KEY = ''
    #ACCESS_TOKEN_SECRET = ''

#    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
 #   file = open(os.path.abspath(path), 'rb')
  #  data = file.read()
   # r = api.request('statuses/update_with_media', {'status':caption}, {'media[]':data})
    #print(r.status_code)


uploadPicToInstagram ("./DSCFAST_.jpg", "We're glad to have @DSCFASTisb by our side, to assist in Digital Media, Machine Learning, and Data Management!\n\nParticipants:\n\n#TheCoronaMap #VolunteerOrganizations #TeamBuilding #TeamWork #Coronavirus #Superheroes")