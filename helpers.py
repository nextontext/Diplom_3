from datetime import datetime

from faker import Faker


fake = Faker()


def generate_user():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")

    return {
        "email": f"{timestamp}_{fake.email()}",
        "password": fake.password(length=10),
        "name": fake.name(),
    }


def generate_user_with_short_password():
    user = generate_user()
    user["password"] = "12345"
    return user
