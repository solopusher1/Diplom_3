class BaseUrls:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

class PageUrls:
    HOME_PAGE = BaseUrls.BASE_URL
    LOGIN_PAGE = BaseUrls.BASE_URL + '/login'
    PASSWORD_RECOVERY_PAGE = BaseUrls.BASE_URL + '/forgot-password'
    RESET_PASSWORD_PAGE = BaseUrls.BASE_URL + '/reset-password'
    PERSONAL_ACCOUNT_PAGE = BaseUrls.BASE_URL + '/account/profile'
    ORDER_HISTORY_PAGE = BaseUrls.BASE_URL + '/account/order-history'
    ORDER_FEED_PAGE = BaseUrls.BASE_URL + '/feed'

class ApiUrls:
    USER_CREATION = BaseUrls.BASE_URL + '/api/auth/register'
    DELETE_USER = BaseUrls.BASE_URL + '/api/auth/'
    LOGIN_USER = BaseUrls.BASE_URL + '/api/auth/login'