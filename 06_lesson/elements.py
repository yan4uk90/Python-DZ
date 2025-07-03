from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(

)))

browser.get("https://ya.ru/")
element = browser.find_element(By.CSS_SELECTOR, '#text')
element.clear()
element.send_keys('Привет')
# browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
# element.send_keys(Keys.RETURN)
sleep(5)

browser.quit()
