from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

accounts_file = open("Accounts/accounts.txt", "r")

line = 0
for line in accounts_file:
        my_username, my_password, my_token = line.replace("\n","").split(":")
        driver = webdriver.Firefox()
        driver.get("http://www.twitch.tv/login")
        elem_user = driver.find_element(By.ID,"login-username")
        elem_passwd = driver.find_element(By.ID,"password-input")
        elem_user.send_keys(my_username)
        elem_passwd.send_keys(my_password)
        elem_passwd.send_keys(Keys.RETURN)
        html = driver.page_source
        soup = BeautifulSoup(html)
        logginTag = soup.find("a", {"id" : "user_display_name"})
        print(logginTag)
        driver.close()