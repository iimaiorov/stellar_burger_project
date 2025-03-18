import dataclasses
from faker import Faker

faker = Faker(locale='en')


@dataclasses.dataclass
class User:
    email: str = None
    password: str = None
    name: str = None

    @staticmethod
    def get_random_user_data():
        email = faker.email()
        password = faker.password(length=10, special_chars=False)
        name = faker.name()
        return User(email=email, password=password, name=name)

    def set_email(self, email):
        self.email = email
        return self

    def set_password(self, password):
        self.password = password
        return self

    def set_name(self, name):
        self.name = name
        return self

    @staticmethod
    def get_email(user):
        return User(email=user.email)

    @staticmethod
    def get_without_password():
        return User(email=faker.email(), name=faker.name())

    @staticmethod
    def get_without_email():
        return User(password=faker.password(length=10, special_chars=False), name=faker.name())

    @staticmethod
    def get_without_name():
        return User(password=faker.password(length=10, special_chars=False), email=faker.email())

    @staticmethod
    def get_with_email_only():
        return User(email=faker.email())

    @staticmethod
    def get_with_name_only():
        return User(name=faker.name())

    @staticmethod
    def get_with_password_only():
        return User(password=faker.password(length=10, special_chars=False))

    @staticmethod
    def get_empty():
        return User()

    def to_json(self):
        return {k: v for k, v in dataclasses.asdict(self).items() if v is not None}
