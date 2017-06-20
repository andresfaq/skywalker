import factory
import factory.fuzzy
import datetime

from baseapp import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# # User Factory
# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     username = factory.Sequence(lambda n: "Usuario%03d" % n)
#     first_name = factory.Faker('first_name')
#     last_name = factory.Faker('last_name')
#     password = make_password('Usuario')
#     is_active = True
#     dni = factory.fuzzy.FuzzyInteger(10000000, 999999999)
#     address = factory.Faker('address')
#     email = factory.Faker('email')
#     birth_date = factory.fuzzy.FuzzyDate(datetime.date(1950, 1, 1), datetime.date(2000, 12, 31))
#     cellphone = factory.fuzzy.FuzzyInteger(1000000, 9999999)
#     phone = factory.fuzzy.FuzzyInteger(100000000, 999999999)

# # Employee Factory
# class EmployeeFactory(UserFactory):
#     class Meta:
#         model = models.Employee

#     username = factory.Sequence(lambda n: "Employee%03d" % n)
#     salary = factory.fuzzy.FuzzyInteger(10000000, 999999999)
#     employee_type = factory.fuzzy.FuzzyChoice(['Employee', 'Administrator'])

# # CLient Factory
# class ClientFactory(UserFactory):
#     class Meta:
#         model = models.Client

#     username = factory.Sequence(lambda n: "Client%03d" % n)

# Employee Factory
class IngredientFactory(factory.Factory):
    class Meta:
        model = models.Ingredient

    name = factory.Sequence(lambda n: "Ingredient Name %03d" % n)
    description = factory.Faker('text', max_nb_chars=200)
    price = factory.fuzzy.FuzzyInteger(1000, 9999)

