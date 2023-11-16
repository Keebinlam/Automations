# # Download Chromedriver, run in OS termonal before running code
# # To extract title and subtitle of each artical
# from selenium import webdriver  # bring in driver
# # this section is required in selenium 4
# from selenium.webdriver.chrome.service import Service
# import pandas as pd

# # website link to take information from
# website = 'https://www.thesun.co.uk/sport/football/'
# # Path to chromedriver, rememeber to run it in terminal for it to work before the code
# path = '/Applications/Python 3.12/chromedriver'

# # defining the driver, we need to create a service in selenim 4
# service = Service(executable_path=path)
# # defining this function with the servide method
# driver = webdriver.Chrome(service=service)
# driver.get(website)  # this is to get the program to work and open chrome

# containers = driver.find_elements(
#     by="xpath", value='//div[@class="teaser__copy-container"]')

# titles = []
# bodys = []
# links = []
# # since containers is a list, it is also iterable. The containers.driver, since it is using the containers valuable, the '.' infront of /a is //div[@class="teaser__copy-container"]
# #this part is go to through each element on the website to match this search, and pull out the text for title and body, and the link for each artical found
# for container in containers:
#     title = container.driver.find_element(by="xpath", value='./a/span').text
#     body = container.driver.find_element(by="xpath", value='./a/h3').text
#     link = container.driver.find_element(
#         by="xpath", value='./a').get_attribute('href')
#     titles.append(titles)
#     bodys.append(bodys)
#     links.append(links)  #this is to add the titles from the for loop back into a list


# my_dict = {'title': titles, 'body': bodys, 'link': links}
# #make dataframe by using pandas, made a library, and put the my_dict library into the dataframe module
# df = pd.Dataframe(my_dict) #set df as a variable

# df.to_csv('headline.csv')#exporting this to cvs file.

# #after all the code has run, the driver will close
# driver.quit()

# body = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]/a/h3')
# ---------------
# go to website, on a blank area, right click and click on inspect to get the right xpath (html elements) for the area you want to extract (developer tool)
# once you find the element you are looking for, click Cntrl F in development tools. You will be able to find element by its xpath
# //div[@class="teaser-item-teaser  small"] in xpath search, it gathered that whole box
# you can go deeper in the div to gather title and text only parts of the html code
# use find_elements Pural, to find all the element that is found in search
# //div[@class="teaser__copy-container"]/a/span to get the title
# //div[@class="teaser__copy-container"]/a/h3 to get the body
# //div[@class="teaser__copy-container"]/a/h3 to get link of artical
# adding .text after the xpath only returns the text and ignore the elements and tags
# you will typcally see the link in the Href attribute within the a tag

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = 'https://www.thesun.co.uk/sport/football/'
path = '/Applications/Python 3.12/chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(
    by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
bodys = []
links = []

for container in containers:
    try:
        title = container.find_element(by="xpath", value='./a/span').text
        body = container.find_element(by="xpath", value='./a/h3').text
        link = container.find_element(
            by="xpath", value='./a').get_attribute('href')
        titles.append(title)
        bodys.append(body)
        links.append(link)
    except Exception as e:
        print("Error processing container:", e)

my_dict = {'title': titles, 'body': bodys, 'link': links}
df = pd.DataFrame(my_dict)

df.to_csv('headline4.csv')

driver.quit()
