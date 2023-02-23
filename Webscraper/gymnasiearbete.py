# import concurrent.futures
import json
import time
# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapeFunctions import *

# from bs4 import BeautifulSoup

# "style-scope ytd-grid-item-renderer" för videos
vid = "/videos"
# "style-scope ytd-rich-video-renderer" för home
home = "/featured" 
channel = "/channels"
newurl = ""

yes_or_no_channel = input("Would you like to use one of our existing channels? Y/N:" ).lower()

if yes_or_no_channel == "n":
    print("somethign")
    channelname = input("Put in the name of the channel: ")
    basicUrl = input("Put in the url of the channel: ")
    appendNameAndUrl(channelname, basicUrl)
elif yes_or_no_channel == "y":
    channelName = input("Put in channelname: ")
    with open('YTchannels.json', 'r') as YTchannels:
        increment = 0
        data = json.load(YTchannels)
        for i in data["channels"]:
            for x in i.keys():
                increment += 1
                if x == channelName:
                    url = data["channels"][increment - 1][channelName][0]["basicurl"]
                    whatToScrape = input("What would you like to webscrape?:\n1:Featured\n2:Videos\n3:Channels ")
                    if whatToScrape == "1":
                        newurl = url + home
                        scrapeHome(newurl)
                    elif whatToScrape == "2":
                        newurl = url + vid
                        scrapeVid(newurl)
                    elif whatToScrape == "3":
                        newurl = url + channel
                        scrapeChannel(newurl)
                    else:
                        print("The only available options are the ones listed, please try again.")      
else:
    print("stupid a fool")