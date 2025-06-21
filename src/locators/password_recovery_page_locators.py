from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input') # Поле "Email"
    RECOVERY_BUTTON = (By.XPATH, './/button[text()="Восстановить"]') # Кнопка "Восстановить"