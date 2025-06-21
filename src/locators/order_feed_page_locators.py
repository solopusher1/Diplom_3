from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    LAST_ORDER = (By.XPATH, './/ul[contains(@class,"OrderFeed_list")]/li[1]/a')  # Последний заказ (верхний в списке)
    ORDER_DETAILS_POPUP = (By.XPATH, './/section[contains(@class,"modal_opened")]/div') # Попап с деталями заказа
    LAST_ORDER_ID = (By.XPATH, './/ul[contains(@class,"OrderFeed_list")]/li[1]/a/div/p[contains(@class,"digits")]')  # ID последнего заказа (верхний в списке)
    ALL_TIME_ORDER_COUNT = (By.XPATH, './/p[text()="Выполнено за все время:"]/parent::div/p[contains(@class,"digits")]') # количество заказов за все время
    TODAY_ORDER_COUNT = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/parent::div/p[contains(@class,"digits")]') # количество заказов за сегодня
    ORDER_IN_WORK = (By.XPATH, './/ul[contains(@class,"orderListReady")]/li') # Первый элемент списка заказов "В работе"