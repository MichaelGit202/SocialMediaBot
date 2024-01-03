from instagramObj import insObj
from redditAPI import redApi

class actionObj: 
                                # parameter object for login info ect.
    def __init__(self, obj, time, parameters):
        self.time = time
        self.obj = obj
        self.param = parameters
        
    def getTime():
        return self.time
    
    def doActions(self):
        print(self.param["type"])
        
        match self.param["type"]:
            case "instagram":
                self.obj.post_video()
            case "reddit":
                self.obj.get_reddit_post(self.param["url"])
            case _:
                print("fail to run action object")
        
        
        