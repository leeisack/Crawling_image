import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

keyword = input('검색할 태그를 입력하세요 : ')
url = 'https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjgwPKzqtXuAhWW62EKHRjtBvcQ_AUoAXoECBEQAw&biw=768&bih=712'.format(keyword)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(1)
SCROLL_PAUSE_SEC = 1.5
more_view = 0

def scroll_down():
    global driver
    global more_view
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_SEC)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            time.sleep(SCROLL_PAUSE_SEC)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if more_view < 10:
                try:
                    more_view += 1
                    # driver.find_element_by_class_name("mye4qd").click()
                    driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
                except:

                #if new_height == last_height:
                    break
            else:
                break
                 
        last_height = new_height




scroll_down()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'})

print('number of img tags: ', len(images))

n = 1
for i in images:
    try:
        imgUrl = i["src"]
    except:
        imgUrl = i["data-src"]
        
    with urllib.request.urlopen(imgUrl) as f:
        with open('./img/' + keyword + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)

    n += 1
