# schedule to run everyday
# turning this py file into an excutable
# install pyinstaller
# use Cd to go to folder of py file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime  # to interact with time
import os  # to interact with computer
import sys

# Getting the path of the excutable that we are going to create
application_path = os.path.dirname(sys.executable)

now = datetime.now()  # indicate on the excutable file of when the date and time it ran
# "String of time" getting time in string format
month_day_year = now.strftime("%m%d%Y")
user_desktop = os.path.expanduser("~/Desktop")

website = 'https://www.thesun.co.uk/sport/football/'
path = 

options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(
    by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
bodys = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/span').text
    body = container.find_element(by="xpath", value='./a/h3').text
    link = container.find_element(
        by="xpath", value='./a').get_attribute('href')
    titles.append(title)
    bodys.append(body)
    links.append(link)


my_dict = {'title': titles, 'body': bodys, 'link': links}
df = pd.DataFrame(my_dict)
filename = f'headline_{month_day_year}.csv'
# Save to Desktop or chosen directory
final_path = os.path.join(user_desktop, filename)
df.to_csv(final_path)
print(f"Saving file to: {final_path}")
driver.quit()
