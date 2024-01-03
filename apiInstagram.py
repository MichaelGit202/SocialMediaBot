from instabot import Bot
from apiGeneric import api
from PIL import Image
import os


class insApi(api):
    def __init__(self, info):
      self.bot = Bot()
      self.credentials = info["login"]
        
        
    def login(self, info):
     
      a = os.getcwd()
      if os.path.isfile(os.getcwd()+ "\\config\\" + self.credentials["username"] + "_uuid_and_cookie.json"):
            os.remove(os.getcwd()+ "\\config\\" + self.credentials["username"] + "_uuid_and_cookie.json")

      self.bot.login(username=self.credentials["username"], password=self.credentials["password"])
      
    def logOut(self, info):
        self.bot.logout()

    def postPicture(self, info):
      comment = info["caption"]
      
      img = Image.open(info["picture"])
      img = img.convert('RGB') 
      # width / heiht
      if (img.width / img.height) < .5:
       width = int(round(((1.5 + (img.width / img.height)) * img.width)))
       img1 = Image.new("RGB", (width, img.height))
       img1.paste(img, (int(round(width/4)), 0))
       img1.save("img.jpg")
      elif (img.height / img.width) < .5:
        height = int(round(((1.5 + (img.height / img.width)) * img.height)))
        img1 = Image.new("RGB", (img.width, height))
        # (/4) when imae is mapped, origin is in top left corner 
        img1.paste(img, (0, int(round((height/4)))))
        img1.save("img.jpg")
      else:  
        img.save("img.jpg")


      #if(img.width > )
      self.bot.upload_photo("img.jpg", caption=info["caption"])
      os.remove("img.jpg.REMOVE_ME")
