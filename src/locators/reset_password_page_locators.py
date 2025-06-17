from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    SHOW_PASSWORD_BUTTON = (By.XPATH, './/div[contains(@class, "input__icon-action")]') # Кнопка "показать/скрыть пароль"
    PASSWORD_FIELD_ACTIVE = (By.XPATH, './/label[text()="Пароль"]/parent::div[contains(@class,"input_status_active")]') # Поле "Пароль" активно (подсвечено)
    PASSWORD_FIELD_NOT_ACTIVE = (By.XPATH, './/label[text()="Пароль"]/parent::div[contains(@class,"input_type_password")]') # Поле "Пароль" не активно (не подсвечено)