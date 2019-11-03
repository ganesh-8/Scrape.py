from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome('/home/ganesh/Downloads/chromedriver',)#options=chrome_options)
browser.get('https://www.flipkart.com')
try:
    abc = browser.find_element_by_xpath("//div[@class ='_3Njdz7']//button[@class = '_2AkmmA _29YdH8']")
    abc.click()
except:
    print("hi")
print(abc)
mob = browser.find_element_by_id('container')
inputs = mob.find_element_by_class_name('LM6RPg')
inputs.send_keys('washing machines')
clicked = mob.find_element_by_class_name('vh79eN').click()
print("---------------------------------------")
#print(mob.text)
# value = browser.find_element_by_class_name('t-0M7P')
# value1 = value.find_element_by_class_name('_3e7xtJ')
# value2 = value1.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]")
# value3 = value2.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]")
# value4 = value3.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div")
# value5 = value4.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div")
# #value6 = value5.find_element_by_class_name('_1UoZlX')
# value6 = value5.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div")
# value7 = value6.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a")
# values = browser.find_element_by_xpath()
#print(value7)

'''browser.find_element_by_class_name('_1Nyybr._30XEf0')
#value = browser.find_element_by_class_name("_1Nyybr")//*[@id="container"]/div/div[3]/div[2]
print(value)
'''
'''container = browser.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div")
box = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div")
'''
# value = browser.find_element_by_class_name('t-0M7P')
# a = value.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]")
# b = a.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]")
# staleElement = True
# while(staleElement):
#     try:
#         c = b.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]")# class = bhgxx2 col-12-12
#         d = c.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div")# class = _3O0U0u
#         #print(e.text)
#         staleElement = False
#     except:
#         print(Exception)
#         staleElement = True
# try:
#     element = WebDriverWait(browser, 10).until(
#         EC._find_element((browser,"_3BTv9X"))
#
#     )
#     #val = WebDriverWait(browser,10).until(EC._find_element(By.CLASS_NAME,))
#     val = browser.find_element_by_xpath(
#         "//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a/div[1]/div[1]/div/div/img")
#     print(val)
# finally:
#
# #browser.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a/div[1]/div[1]/div/div/img")
#//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[4]/div/div/div/a/div[1]/div[1]/div/div/img
browser.implicitly_wait(130)
block = browser.find_element_by_class_name('_3O0U0u')

count =1
name = browser.find_elements_by_class_name('_3wU53n')
data = browser.find_elements_by_class_name('vFw0gD')
href = browser.find_elements_by_class_name('_31qSD5')
rate = browser.find_elements_by_class_name('_1vC4OE._2rQ-NK')
j=0
for i in range(2,26):
    browser.implicitly_wait(120)
    browser.execute_script("window.scrollBy(200,500)")

    i = str(i)

    s = ("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div["+i+"]/div/div/div/a/div[1]/div[1]/div/div/img")

    ing = block.find_element_by_xpath(s)
    print(name[j].text)
    print(data[j].text)
    print(rate[j].text)
    abc = href[j]
    print(abc.get_attribute('href'))
    print(ing.get_attribute('src'))
    print("---------------------------------------------------------------------------------------------------------------------")
    j = j+1
    count = count+1
print(count)

browser.close()
