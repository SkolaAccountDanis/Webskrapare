# import json
import json
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup


# test = input("Choose category: 'random', 'ting' or 'test'")

# if test == 'test':
#     data = input("Please put in the data you want into test: ")
#     x = {'test': data}
# elif test == 'random':
#     data = input("Please put in the data you want into random: ")
# elif test == 'ting':
#     data = input("Please put in the data you want into ting: ")
# else:
#     print("you did something wrong")


# def appendNameAndUrl(name, url):
#     with open('YTchannels.json', 'r') as YTchannels:
#         data = json.loads(YTchannels.read())

#     data['channels'].append({"name": name, "url": url})  

#     with open('YTchannels.json', "w") as file:
#         file.write(json.dumps(data, indent=2))

# appendNameAndUrl("MrBeast", "potato")


# data['channels'][channelID]['name'] = name



url2 = "https://www.youtube.com/@MrBeast"
vid = "/videos"
home = "/featured"
channel = "/channels"
newurl = ""
hej = ""
# if hej == "1":

#     newurl = url2+vid
#     print(newurl)
# elif hej == "2":
#     newurl = url2+home
#     print(newurl)
    
# elif hej == "3":
#     newurl = url2+channel
#     print(newurl)
# else:
#     print("you did not typ in a valid awnser pls try agien")

def scrape(newurl, hej):
    
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(newurl)
    
    start = time.time()
    driver.implicitly_wait(3)

    deny = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button')
    deny.click()

    hem = driver.find_elements(By.CLASS_NAME, hej)

    for video in hem:
        title = video.find_element(By.XPATH, './/*[@id="video-title"]').text
        views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
        date = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
        print('Title:', title, '\n' 'Views:', views, '\n''Date:', date, '\n')
    driver.quit()

    end = time.time()
    sumTime = int(end-start)
    print('The scraping took', sumTime ,'seconds.')



choice = input()
if choice == "1":
    newurl = url2 + vid
    hej = "style-scope ytd-grid-item-renderer"
    scrape(newurl, hej)
elif choice == "2":
    newurl = url2 + home
    hej = "style-scope ytd-rich-video-renderer"
    scrape(newurl, hej)
