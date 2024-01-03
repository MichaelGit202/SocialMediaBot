from redditAPI import redApi
from instapy_cli import client
import time
from PIL import Image
import os

class insObj:
  
  def __init__(self, usr, pas):
    #self.bot = Bot()
    self.username = usr
    self.password = pas
    self.image = ""
    self.caption = ""
    self.loggedin = 0
    self.bot = client(username=usr,password=pas)
    
    
  def login(self):
    #os.remove("config/test123412311234125_uuid_and_cookie.json")
    #self.bot.login(username=self.username, password=self.password)
    #self.bot.login()
    self.loggedin = 1
    
  def logout(self):
      self.bot.logout()
      self.loggedin = 0

  def post_to_instagram(self, image_path):
      #username = "test123412311234125"
      #password = "moneyehyea1231234"
      #image_path = "cat1.png" 
      #caption = "cat."
      
      img = Image.open(image_path)
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


      #bot.login(username=username, password=password)


      self.bot.upload("img.jpg", caption=self.caption)
  
  
  def post_video(self):
      self.bot.upload("cat1.png", "caption")
