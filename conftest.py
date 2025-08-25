import pytest
from data.helpers import RandomData as R

@pytest.fixture
def courier():
    return {
        "login": R.generate_random_string(5),
        "password": R.generate_random_string(9),
        "firstName": R.generate_random_string(4),
    }
@pytest.fixture
def order():
    return {
        "firstName": R.generate_random_string(6),
        "lastName": R.generate_random_string(6),
        "address": R.generate_random_string(4),
        "metroStation": R.generate_random_number(),
        "phone": R.generate_random_phone(),
        "rentTime": R.generate_random_number(),
        "comment": R.generate_random_string(13),
        "color": R.generate_random_color()
    }