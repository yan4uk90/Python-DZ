from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))

driver.maximize_window()
driver.get('http://uitestingplayground.com/classattr')

for i in range(1):
    driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.refresh()

sleep(10)
