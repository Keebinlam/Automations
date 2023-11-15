#Download Chromedriver for current chrome version. Go into System files, and run "chromedriver" in OS terminal before running code
#Pip3 install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = '/Applications/Python 3.12/chromedriver'  # introduce path here
