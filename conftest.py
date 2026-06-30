import pytest
import requests

from helpers import generate_user
from urls import BASE_URL, REGISTER_USER, USER
from utils.webdriver_factory import WebDriverFactory


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = WebDriverFactory.get_webdriver(request.param)
    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def create_user():
    user_data = generate_user()
    
    response = requests.post(REGISTER_USER, json=user_data)
    response_body = response.json()

    user = {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "access_token": response_body["accessToken"],
    }

    yield user

    requests.delete(USER, headers={"Authorization": user["access_token"]})
