import loginKey
login = loginKey.data

week = 'w02'
target_str = week + '_201'
driverPath = './chromedriver'
downloadPath = '/home/yssong/auto_score/source/'
sleeptime = 0.1

from bs4 import BeautifulSoup
import requests
import time
import os
from selenium import webdriver
from pyvirtualdisplay import Display

os.system("rm -r ./source/*")
option = webdriver.ChromeOptions()
option.add_experimental_option("prefs", {
    "download.default_directory": downloadPath
})
driver = webdriver.Chrome(driverPath, chrome_options=option)
display = Display(visible=0, size=(1920,1080))
time.sleep(sleeptime)

driver.get("https://ssl.uos.ac.kr/moodle/mod/assignment/index.php?id=7")
time.sleep(sleeptime)

driver.find_element_by_xpath('//*[@id="details-button"]').click()
time.sleep(sleeptime)

driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
time.sleep(sleeptime)

driver.find_element_by_name('username').send_keys(login.get("id"))
driver.find_element_by_name('password').send_keys(login.get("pw"))
driver.find_element_by_xpath('//*[@id="login"]/div/div[5]/input[2]').click()
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')
all_paragraph = soup.find_all('a')
cnt = 0
for para in all_paragraph:
    if target_str in str(para):
        cnt += 1
        href = para.get('href')
        #print(href)
        r = driver.get(str(href))

print("parsed count : " + str(cnt))
cnt = 0

for anyFile in os.listdir("./source/"):
    if ".tar" in str(anyFile):
        #print("processing " + str(anyFile))
        os.system("tar -xvf ./source/" + anyFile + " -C ./source/ > /dev/null")
        time.sleep(0.1)
        cnt += 1
time.sleep(1.0)
os.system("rm ./source/*.tar > /dev/null")

print("decompress count : " + str(cnt))