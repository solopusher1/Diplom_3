from selenium.webdriver.common.by import By

class MainPageLocators:
    HEADER_MAKE_YOUR_BURGER = (By.XPATH, './/h1[text()="Соберите бургер"]')  # Заголовок "Соберите бургер"
    RANDOM_INGREDIENT = (By.XPATH, './/ul[contains(@class,"BurgerIngredients")]/a') # Первый ингредиент из первого раздела
    RANDOM_INGREDIENT_COUNTER = (By.XPATH, './/ul[contains(@class,"BurgerIngredients")]//p[contains(@class,"counter__num")]') # Счетчик первого ингредиента из первого раздела
    INGREDIENT_DETAILS_POPUP_HEADER = (By.XPATH, './/h2[contains(@class,"modal__title") and text()="Детали ингредиента"]') # Заголовок попапа "Детали ингредиента"
    INGREDIENT_DETAILS_POPUP_CLOSE_BUTTON = (By.XPATH, './/button[contains(@class,"modal__close")]') # Крестик попапа "Детали ингредиента"
    BURGER_CONSTRUCTOR_SECTION = (By.XPATH, './/section[contains(@class,"BurgerConstructor")]/ul') # Конструктор
    MAKE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # Кнопка "Оформить заказ" (пользователь авторизован)
    ORDER_ID = (By.XPATH, './/section[contains(@class,"modal_opened")]//h2') # ID заказа на попапе "Заказ оформлен"
    LOADING_PAGE_ANIMATION = (By.XPATH, './/img[contains(@class,"modal__loading")]/parent::div') # Анимация загрузки страницы
    ORDER_WAS_PLACED_POPUP_CLOSE_BUTTON = (By.XPATH, './/button[contains(@class,"modal__close")]') # Крестик попапа "Заказ оформлен"