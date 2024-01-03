import subprocess
import json
from bs4 import BeautifulSoup
import requests
import sys

url = "https://www.reddit.com/r/Awww/comments/15lrhxp/moments_of_tenderness/" #sys.argv[1]    # gets the url passed in the command-line
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url,headers = headers)


post_id = url[url.find('comments/') + 9:]
post_id = f"t3_{post_id[:post_id.find('/')]}"


if(response.status_code == 200):    # checking if the server responded with OK
  soup = BeautifulSoup(response.text,'lxml')
  # I looked up the original code of the reddit page 
  # to find where all the data was and it was in a script tag
  # with the id set to 'data'
  required_js = soup.find('script',id='data') 
  
  json_data = json.loads(required_js.text.replace('window.___r = ','')[:-1])
  # 'window.___r = ' and a semicolon at the end of the text were removed
  # to get the data as json
  title = json_data['posts']['models'][post_id]['title']
  title = title.replace(' ','_')
  dash_url = json_data['posts']['models'][post_id]['media']['dashUrl']
  height  = json_data['posts']['models'][post_id]['media']['height']
  dash_url = dash_url[:int(dash_url.find('DASH')) + 4]
  # the dash URL is the main URL we need to search for
  # height is used to find the best quality of video available
  video_url = f'{dash_url}_{height}.mp4'    # this URL will be used to download the video
  audio_url = f'{dash_url}_audio.mp4'    # this URL will be used to download the audio part
  
  
  with open(f'{title}_video.mp4','wb') as file:
    print('Downloading Video...',end='',flush = True)
    response = requests.get(video_url,headers=headers)
    if(response.status_code == 200):
        file.write(response.content)
        print('\rVideo Downloaded...!')
    else:
        print('\rVideo Download Failed..!')

  with open(f'{title}_audio.mp3','wb') as file:
    print('Downloading Audio...',end = '',flush = True)
    response = requests.get(audio_url,headers=headers)
    if(response.status_code == 200):
        file.write(response.content)
        print('\rAudio Downloaded...!')
    else:
        print('\rAudio Download Failed..!')