# import concurrent.futures
import json
import time
# import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def scrapeHome(newurl):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(newurl)
    
    start = time.time()
    driver.implicitly_wait(3)

    deny = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button')
    deny.click()

    hem = driver.find_elements(By.CLASS_NAME, "style-scope ytd-grid-video-renderer")

    for video in hem:
        title = video.find_element(By.XPATH, './/*[@id="video-title"]').text
        views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
        date = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
        print('Title:', title, '\n' 'Views:', views, '\n''Date:', date, '\n')
    driver.quit()

    end = time.time()
    sumTime = int(end-start)
    print('The scraping took', sumTime ,'seconds.')
def scrapeVid(newurl):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(newurl)
    
    start = time.time()
    driver.implicitly_wait(3)

    deny = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button')
    deny.click()


    videotab = driver.find_elements(By.CLASS_NAME, "style-scope ytd-rich-item-renderer")

    for videos in videotab:
       title = videos.find_element(By.XPATH, './/*[@id="video-title"]').text
       views = videos.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
       date = videos.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
       print('Title:', title, '\n' 'Views:', views, '\n''Date:', date, '\n')
    driver.quit()

    end = time.time()
    sumTime = int(end-start)
    print('The scraping took', sumTime ,'seconds.')
def scrapeChannel(newurl):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(newurl)
    
    start = time.time()
    driver.implicitly_wait(3)

    deny = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button')
    deny.click()

    channels = driver.find_elements(By.CLASS_NAME, "style-scope ytd-grid-channel-renderer")

    for chanel in channels:
        chanelname = chanel.find_element(By.XPATH, './/*[@id="title"]').text
        chanelsubs = chanel.find_element(By.XPATH, './/*[@id="thumbnail-attribution"]').text
        print('Chanel Name', chanelname, '\n' 'Subscribers', chanelsubs, '\n')
    driver.quit()

    end = time.time()
    sumTime = int(end-start)
    print('The scraping took', sumTime ,'seconds.')


def appendNameAndUrl(name, basicurl):
    with open('YTchannels.json', 'r') as YTchannels:
        data = json.loads(YTchannels.read())

    data['channels'].append({name: [{"basicurl": basicurl}]})  

    with open('YTchannels.json', "w") as file:
        file.write(json.dumps(data, indent=2))
