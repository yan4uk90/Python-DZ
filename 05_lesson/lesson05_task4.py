from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/login')

username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('tomsmith')
password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('SuperSecretPassword!')
login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
login_button.click()

success_message = driver.find_element(By.ID, "flash")
print(success_message.text)

sleep(5)
driver.quit()
