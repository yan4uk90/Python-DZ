
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class internet_shop:
    def __init__(self, driver, url: str):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    def username(self, username: str):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys
        (username)

    def password(self, password: str):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys
        (password)

    def button(self, locator):
        self._driver.find_element(By.CSS_SELECTOR, locator).click()

    def post(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(
            "Yana")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(
            "Gotovtseva")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(
            "112233")

    def price(self):
        txt = self._driver.find_element
        (By.CSS_SELECTOR, ".summary_total_label").text
        return txt


def test_swag_labs():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager(
    ).install()))

    # Логин
    magazine_swag_labs = internet_shop(browser, "https://www.saucedemo.com/")
    magazine_swag_labs.username("standard_user")
    magazine_swag_labs.password("secret_sauce")
    magazine_swag_labs.button("#login-button")

    # Добавление товаров в корзину
    magazine_swag_labs = internet_shop
    (browser, 'https://www.saucedemo.com/inventory.html')
    magazine_swag_labs.button("#add-to-cart-sauce-labs-backpack")
    magazine_swag_labs.button("#add-to-cart-sauce-labs-bolt-t-shirt")
    magazine_swag_labs.button("#add-to-cart-sauce-labs-onesie")

    # Переход в корзину и оформление заказа
    magazine_swag_labs = internet_shop
    (browser, 'https://www.saucedemo.com/cart.html')
    magazine_swag_labs.button("#shopping_cart_container")
    magazine_swag_labs.button("#checkout")

    # Заполнение данных на странице оформления заказа
    magazine_swag_labs = internet_shop
    (browser, 'https://www.saucedemo.com/checkout-step-one.html')
    magazine_swag_labs.post()
    magazine_swag_labs.button("#continue")

    # Подтверждение заказа и проверка суммы
    magazine_swag_labs = internet_shop
    (browser, "https://www.saucedemo.com/checkout-step-two.html")
    summ = magazine_swag_labs.price()

    assert summ == "Total: $58.29"

    browser.quit()
