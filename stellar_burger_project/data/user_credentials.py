import dataclasses

from faker import Faker

faker = Faker(locale='en')


@dataclasses.dataclass
class UserCredentials:
    email: str = None
    password: str = None

    @classmethod
    def from_user(cls, user):
        return cls(email=user.email, password=user.password)

    def set_email(self, email):
        self.email = email
        return self

    def set_password(self, password):
        self.password = password
        return self

    @classmethod
    def get_user_authorization_with_email_only(cls, user):
        return cls().set_email(user.email)

    @classmethod
    def get_user_authorization_with_password_only(cls, user):
        return cls().set_password(user.password)

    @classmethod
    def get_user_authorization_with_only_valid_email(cls, user):
        return cls().set_email(user.email).set_password(faker.password())

    @classmethod
    def get_user_authorization_with_only_valid_password(cls, user):
        return cls().set_email(faker.email()).set_password(user.password)

    @classmethod
    def get_user_authorization_with_empty(cls, user):
        return cls().set_email(None).set_password(None)

    def to_json(self):
        return dataclasses.asdict(self)
