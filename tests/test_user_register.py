import pytest
import allure


from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.epic("User registration cases")
class TestUserRegister(BaseCase):
    # def setup(self):
    #     base_part = "learnqa"
    #     domain = "example.com"
    #     random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    #     self.email = f"{base_part}{random_part}@{domain}"

    @allure.description("Positive: User created successfully")
    def test_create_new_user_successfully(self):
        data = self.prepare_registration_data()
        # data = {
        #     'username': 'learnqa',
        #     'password': '123',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': self.email
        # }

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    @allure.description("Negative: Creating user with existing email")
    def test_create_user_with_existing_email(self):

        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        data = {
        'username': 'learnqa',
        'password': '123',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': email
         }

        response = MyRequests.post("/user/", data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email 'vinkotov@example.com' already exists"

    @allure.description("Negative: Creating user with wrong email format")
    def test_create_user_with_wrong_format(self):

        email = 'vinkotov.example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        # Assertions.assert_json_has_key(response, 'id')

    @allure.description("Negative: Creating user with one character email address")
    def test_create_user_with_one_char(self):

        email = 'v'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        # Assertions.assert_json_has_key(response, 'id')
    @allure.description("Negative: Creating user with more then 255 characters email address")
    def test_create_user_with_260_char(self):

        email = 'v'*260
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        # Assertions.assert_json_has_key(response, 'id')

    user_fields = [
        ('username'),
        ('password'),
        ('firstName'),
        ('lastName'),
        ('email')
    ]
    @allure.description("Negative: Creating user with some empty fields")
    @pytest.mark.parametrize("fields", user_fields)
    def test_create_user_without_some_field(self, fields):

        data = self.prepare_registration_data()

        data[fields] = None
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
