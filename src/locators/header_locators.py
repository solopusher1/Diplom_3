from selenium.webdriver.common.by import By

class HeaderLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/header//p[text()="Личный Кабинет"]')  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]/parent::a') # Кнопка "Конструктор"
    ORDER_FEED_BUTTON = (By.XPATH, './/p[text()="Лента Заказов"]') # Кнопка "Лента заказов"