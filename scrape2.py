from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
s = input('Enter the text\n')
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
browser = webdriver.Chrome('/home/ganesh/Downloads/chromedriver',options=chrome_options)

browser.get('https://www.flipkart.com')
try:
    abc = browser.find_element_by_xpath("//div[@class ='_3Njdz7']//button[@class = '_2AkmmA _29YdH8']")
    abc.click()
except:
    print("hi")
#print(abc)
mob = browser.find_element_by_id('container')
inputs = mob.find_element_by_class_name('LM6RPg')
inputs.send_keys(s)
clicked = mob.find_element_by_class_name('vh79eN').click()
#print("---------------------------------------")
browser.implicitly_wait(30)
j = 2
test = browser.find_element_by_class_name('_3O0U0u')
divide = test.find_element_by_xpath(".//*")
width = divide.get_attribute('style')
abc = width.split()
value = abc[1]
if value == '25%;':
    for whole in browser.find_elements_by_class_name('_3O0U0u'):
        for i in range(1,5):
            i = str(i)
            j = str(j)
            data = whole.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div["+j+"]/div/div["+i+"]")
            browser.implicitly_wait(10)
            print(data.text)
            link = data.find_element_by_tag_name('a')
            print(link.get_attribute('href'))
            img_link = data.find_element_by_tag_name('img')
            print(img_link.get_attribute('src'))
            rate = data.find_element_by_class_name('_1vC4OE')
            browser.implicitly_wait(20)
            print(rate.text)
            print("========================================================================================")
        browser.implicitly_wait(30)
        browser.execute_script("window.scrollBy(200,500)")
        j = int(j)
        j = j+1

elif value == '100%;':
    block = browser.find_element_by_class_name('_3O0U0u')

    count = 1
    name = browser.find_elements_by_class_name('_3wU53n')
    data = browser.find_elements_by_class_name('vFw0gD')
    href = browser.find_elements_by_class_name('_31qSD5')
    rate = browser.find_elements_by_class_name('_1vC4OE._2rQ-NK')
    j = 0
    for i in range(2, 26):
        browser.implicitly_wait(120)
        browser.execute_script("window.scrollBy(200,500)")

        i = str(i)

        s = (
                    "//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[" + i + "]/div/div/div/a/div[1]/div[1]/div/div/img")

        ing = block.find_element_by_xpath(s)
        print(name[j].text)
        print(data[j].text)
        print(rate[j].text)
        abc = href[j]
        print(abc.get_attribute('href'))
        print(ing.get_attribute('src'))
        print(
            "---------------------------------------------------------------------------------------------------------------------")
        j = j + 1
        count = count + 1
    print(count)

browser.close()

