import time
from redditAPI import redApi
from instagramObj import insObj
from actionObj import actionObj
import random
import json
from instapy_cli import client
from tiktok_uploader.auth import AuthBackend
from tiktok_uploader.upload import upload_video

#hardcoded R/awww to instagram script
if __name__ == "__main__":

    #reddit_url = "https://www.reddit.com/r/awww/"
    #j = 0
    
    #get_reddit_post(reddit_url)
    
    #insbot = insObj("test123412311234125","moneyehyea1231234", 10000)
    #insbot.login()
    #insbot.post_to_instagram("cat1.png")
 
 
    #Startup sequence
        # for now just login 1 insta account and schedule posts
    
    insta = insObj("test123412311234125","moneyehyea1231234")
    redd = redApi()
    
    
    pR = {
        "type" : "reddit",
        "url" : "https://www.reddit.com/r/awww/",
    }
    
    pI = {
        "type" : "instagram",
        "username" : "test123412311234125",
        "password" : "moneyehyea1231234",
        "imagePath" : "cat1.png",
        "caption" : "asdasdad"
    }
    
    
  

    username = 'test123412311234125' #your username
    password = 'moneyehyea1231234' #your password 
    image = 'cat1.png' #here you can put the image directory
    text = 'Here you can put your caption for the post'
    
    with client(username, password) as cli:
       cli.upload(image, text)
    
    #ac1 = actionObj(insta, 10, pI)
    #ac2 = actionObj(redd, 10, pR)
    
    #ac1.doActions()
    #ac2.doActions()

    #note with this setup you cant schedule anything past 24 hours 
   #curTime = time.localtime()
   #
   #ptime = 16
   #wait = ptime - curTime.tm_hour
   #wmin = random.randint(0,59) # random time within hour
   #print(wait)
   #flag = 0
   #
   #while(flag == 0):
   #    if(wait < 0):
   #        print("a")
   #        #code to run commands during,
   #        # 1. post
   #        # 2. scrape
   #    else:
   #         time.sleep((ptime * 60) + wmin)
            
    
    