from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time


browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_element(By.XPATH,"//*[@id='layers']/div/div[1]/div/div/div/div/div[2]/div/div/div[1]")

giris_yap.click()

time.sleep(3)

username = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

username.send_keys("yourusername")

time.sleep(3)

login = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")

login.click()

time.sleep(3)

password = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")

password.send_keys("yourpassword")

time.sleep(3)

final_login = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")

final_login.click()

time.sleep(5)

searchArea = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")

searchArea.send_keys("Hashtag you want to search")

time.sleep(3)

searchArea.send_keys(Keys.RETURN)

time.sleep(7)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True
time.sleep(5)


tweets = []


elements = browser.find_elements(By.CSS_SELECTOR,".css-901oao.r-1nao33i.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")

for element in elements:
    tweets.append(element.text)

tweetCount = 1

with open("tweets.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("**********************************\n")
        tweetCount += 1

browser.close()
