import requests 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import uuid
from PIL import Image
import time

class redApi:
    
    
    def get_reddit_post(self,url):  

        firefox_options = Options()  
        firefox_options.add_argument("--disable-notifications")

        # Set up the Chrome WebDriver
        service = Service(executable_path='geckodriver')
        driver = webdriver.Firefox(service=service,options=firefox_options)
        driver.get(url)



        # Wait for the page to load (adjust sleep time as needed)
        time.sleep(5)
        i = 0

        while(i < 5):
            driver.execute_script("window.scrollTo(0, 50000)")
            time.sleep(1)
            i += 1

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        posts = soup.select('a[slot="full-post-link"]')
        print(posts)

        hrefs_list = [element['href'] for element in posts if 'href' in element.attrs]



        print(hrefs_list)
        print(len(hrefs_list))


        hist = self.loadHistory();
        #gpt code that removes items found in hist list
        #hopefully better than double for loop :p
        hrefs_list = [item for item in hrefs_list if item not in hist]

        self.writeHistory(hrefs_list)


        for link in hrefs_list:
            flag =  0
            tries = 0

            while(flag != 1):
                try:

                    driver.get("https://www.reddit.com" + link)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    time.sleep(1)
                    subred = soup.find_all('shreddit-post')
                    type = subred[0]["post-type"]

                    if(type == "video"):
                    
                            video = soup.find('shreddit-player').get('src')
                            #title = soup.find('div', {'slot':'title'}).get_text().strip()
                            linkspl = link.split('/')
                            title = linkspl[len(linkspl) - 2 ]
                            print(title)
                            print(video)
                            name = str(uuid.uuid1())
                            if("https://packaged-media" in video):
                                download_file(video,"videos/" + name)
                                with open("videos/captions.txt", "+a") as cap:
                                  cap.write(name + " " + title + "\n")

                    flag = 1

                except Exception as e:
                    tries += 1

                    if(tries < 5):
                        flag = 1
                    time.sleep(5)
                    print("error: ")
                    print(e)

        #video = soup.find("video")#.get("src") post-type=

        #print(video)

        #the list method does not work IG 

        #post_title.__getattribute__("permalink")
        #post_author = soup.select_one('span[class="_2tbHP6ZydRpjI44J3syuqC"]').text.strip()
        #post_content = soup.select_one('div[class="rpBJOHq2PR60pnwJlUyP0"]').text.strip()

        #print("Title:")
        #print(post_title)
        #print("Author:", post_author)
        #print("Content:", post_content)

        # Close the browser
        input("pause")
        driver.quit()
        
    def download_file(url,filename):
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian       
        return filename


    def loadHistory(self):
        hist_arr = []
        with open("videos/history.txt", "r") as f:
            hist_arr = [line.strip() for line in f.readlines()]
        f.close()
        return hist_arr

    def writeHistory(self, inparr):
        with open("videos/history.txt", "w") as f:
            for line in inparr:
                f.write(line + '\n')
        f.close()
