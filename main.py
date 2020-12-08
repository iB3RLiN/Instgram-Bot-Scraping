'''
        this code to get all posts links from target Instagram account and automatic login
                             by user or cookies.json file.
                                   CoDe By BeRLiN
                                 Twitter @iAhmedika
'''

from config import *
from selenium import webdriver
import time
import keyboard
import os
import json
from config import *
from pathlib import Path


try:
    current_path = os.path.dirname(os.path.abspath(__file__))
except:
    current_path = '.'

gecko = r"C:\Users\BeRLiN\Desktop\Automation Project\geckodriver.exe"
browser = webdriver.Firefox(executable_path=gecko)

def instagram_login(browser):

    gecko = r"C:\Users\BeRLiN\Desktop\Automation Project\geckodriver.exe"
    browser = webdriver.Firefox(executable_path=gecko)
    browser.get(instagram_login_page)
    time.sleep(20)

    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').click()
    keyboard.write(instagram_username, delay=0.25, restore_state_after=True)
    time.sleep(3)
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').click()
    keyboard.write(instagram_password, delay=0.25, restore_state_after=True)
    time.sleep(3)
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div'
    ).click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    cookies = browser.get_cookies()
    cookies_file = open(f'{current_path}/{instagram_cookies_path}', 'w', encoding='utf8')
    cookies_file.write(json.dumps(cookies))
    cookies_file.close()

browser.get(instagram_url)
time.sleep(5)
cookies = ''
cookies_file = f'{current_path}/{instagram_cookies_path}'
if Path(cookies_file).is_file():
    with open(cookies_file, 'r', encoding='utf8') as cookies_file:
        cookies = cookies_file.read()

if cookies != '':
    cookies = json.loads(cookies)
    if len(cookies) > 0:
        for cookie in cookies:
            browser.add_cookie(cookie)
    time.sleep(5)
    browser.get(f'{instagram_url}')
browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click() #noiti off
time.sleep(5)
browser.get(targit_list)
time.sleep(5)

lenOfPage = browser.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while (match == False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True

posts = []
links = browser.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)

print(posts)
print(len(posts))







