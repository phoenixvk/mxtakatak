import requests
import re
from json import JSONDecoder
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


#enter user profile link
url = 'https://www.mxtakatak.com/12112868004850123567790'

#use Proxy If needed


# proxy_host = ""
# proxy_port = ""
# proxy_auth = ""
# proxies = {
#        "https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
#        "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)
# }

# #User Agent
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

# r = requests.get(url, headers=headers)



driver = webdriver.Firefox(executable_path=r'C:\Users\vaibhav\Downloads\geck\geckodriver.exe')
driver.get(url)

count = 0
while count < 4 :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    count+=1
    print(count)

html = driver.page_source


soup = BeautifulSoup(html, 'html.parser')
text = 'window._state'
cardviews = soup.find('div',class_="cards-view")
all_cards_divs =  cardviews.find_all('div',class_="feed-card-container")

with open('C:\\Users\\vaibhav\\Desktop\\pythonscrape\\csvfile.csv','w') as file:
    for card_div in all_cards_divs :
        div_tag = card_div.find('div',class_='image-card blur-img')
        img_tag = div_tag.next
        print(img_tag['src'])
        src_img = img_tag['src']
        file.write(src_img)
        file.write('\n')
file.close

