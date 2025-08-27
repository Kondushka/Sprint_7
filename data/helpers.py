import random
import string

class RandomData:
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_random_number():
            nomber = random.randint(1,200)
            return nomber

    def generate_random_phone():
        nomber = f'+7{random.randint(9000000000, 9999999999)}'
        return str(nomber)

    def generate_random_color():
        color = random.choice(["BLACK", "GREY", ""])

class TextResponse:
    DUPLICATE_LOGIN = "Этот логин уже используется. Попробуйте другой."
    MISSING_FIELDS = "Недостаточно данных для создания учетной записи"
    LOGIN_DATA_MISSING = "Недостаточно данных для входа"
    USER_NOT_FOUND = "Учетная запись не найдена"