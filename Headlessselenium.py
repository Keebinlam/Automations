from selenium import webdriver  # bring in driver
# this section is required in selenium 4
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

# website link to take information from
website = 'https://www.thesun.co.uk/sport/football/'
# Path to chromedriver, rememeber to run it in terminal for it to work before the code
path = ''

options = Options()
options.headless = True
# defining the driver, we need to create a service in selenim 4
service = Service(executable_path=path)
# defining this function with the servide method
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)  # this is to get the program to work and open chrome

containers = driver.find_elements(
    by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
bodys = []
links = []
# since containers is a list, it is also iterable. The containers.driver, since it is using the containers valuable, the '.' infront of /a is //div[@class="teaser__copy-container"]
# this part is go to through each element on the website to match this search, and pull out the text for title and body, and the link for each artical found
for container in containers:
    title = container.find_element(by="xpath", value='./a/span').text
    body = container.find_element(by="xpath", value='./a/h3').text
    link = container.find_element(
        by="xpath", value='./a').get_attribute('href')
    titles.append(title)
    bodys.append(body)
    # this is to add the titles from the for loop back into a list
    links.append(link)


my_dict = {'title': titles, 'body': bodys, 'link': links}
# make dataframe by using pandas, made a library, and put the my_dict library into the dataframe module
df = pd.DataFrame(my_dict)  # set df as a variable

df.to_csv('headline_headless2.csv')  # exporting this to cvs file.

# after all the code has run, the driver will close
driver.quit()
