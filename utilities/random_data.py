from faker import Faker


class RandomData:

    fake = Faker()

    @staticmethod
    def email():

        return RandomData.fake.email()

    @staticmethod
    def username():

        return RandomData.fake.user_name()

    @staticmethod
    def phone():

        return RandomData.fake.phone_number()