from selenium import webdriver
import time


def site_login(browser):
    browser.find_element_by_id('os_username').send_keys('tomas.pustka@quest.com')
    browser.find_element_by_id('os_password').send_keys('Warlord555')
    browser.find_element_by_id('loginButton').click()




browser = webdriver.Chrome()
browser.get("https://wiki.labs.quest.com/display/TE/2018-10-16+Meeting+notes+-+Common+staff+meeting")

site_login(browser)

while True:
    browser.refresh()
    time.sleep(5)