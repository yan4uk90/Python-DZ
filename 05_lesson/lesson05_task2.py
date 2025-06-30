from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()
                                                ))

driver.maximize_window()
driver.get('http://uitestingplayground.com/dynamicid')

for i in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()

sleep(10)
