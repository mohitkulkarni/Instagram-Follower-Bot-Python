from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time

chrome_driver_path = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
instagram_url = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(instagram_url)

    def login(self, username, password):
        time.sleep(5)
        user_id = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_id.send_keys(username)
        user_pass = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        user_pass.send_keys(password)
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)
        print("login success.....")
        exit1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        exit1.click()
        print("exit location")
        time.sleep(5)
        exit2 = self.driver.find_element_by_css_selector(".aOOlW")
        exit2.click()
        print("exit notification")

    def find_followers(self, account_name):
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div/span[2]')
        search.click()
        print("click search")
        time.sleep(2)
        user_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        user_input.send_keys(account_name)
        time.sleep(2)
        user_input.send_keys(Keys.ENTER)
        user_input.send_keys(Keys.ENTER)
        print("Enter Search bar")
        time.sleep(4)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        print("click on followers")

        time.sleep(4)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_css_selector('.aOOlW')
                print("cancel")
                cancel_button.click()
