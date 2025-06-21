from selenium.webdriver.common.by import By

class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, './/main//a[text()="Восстановить пароль"]')  # Кнопка "Восстановить пароль"
    EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/parent::div/input')  # Поле ввода "Email"
    PASSWORD_INPUT = (By.NAME, 'Пароль')  # Поле ввода "Пароль"
    ENTER_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # Кнопка "Войти"