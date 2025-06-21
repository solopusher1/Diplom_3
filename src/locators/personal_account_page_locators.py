from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    ORDER_HISTORY_BUTTON = (By.XPATH, './/a[text()="История заказов"]')  # Кнопка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')  # Кнопка "Выход"