class Urls:
    HOME_URL_API = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    CREATE_COURIER_URL = f"{HOME_URL_API}courier"
    LOGIN_COURIER_URL = f"{CREATE_COURIER_URL}/login"
    ID_COURIER_URL = f"{CREATE_COURIER_URL}/"
    ORDER_URL = f"{HOME_URL_API}orders"
    CANCEL_ORDER_URL = f"{ORDER_URL}/cancel"

    