import allure
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы по url')
    def get(self, url):
        self.driver.get(url)

    @allure.step('Ожидание соответствия текущего url требуемому значению')
    def wait_url_to_be(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    @allure.step('Получение текста элемента по его локатору')
    def get_text_of_the_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Заполнение поля требуемым значением')
    def filling_the_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Клик по элементу с использованием нескольких попыток в случае вызова исключения')
    def click_to_element_few_tries(self, locator):
        attempts = 3
        for _ in range(attempts):
            try:
                self.driver.find_element(*locator).click()
                break  # Успешный клик, завершаем цикл
            except ElementClickInterceptedException:
                sleep(2)  # Ожидание перед следующей попыткой

    @allure.step('Ожидание невидимости элемента')
    def wait_for_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        drag_and_drop(self.driver, source, target)

    @allure.step('Ожидание видимости требуемого текстового значения на элементе')
    def wait_for_text_to_be_present_in_element(self, locator, text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))