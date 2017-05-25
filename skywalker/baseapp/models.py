from django.db import models
from accounts.models import Employee, Client

# Ingredient Class
class Ingredient(models.Model):
    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=2000, null=True, blank=True)
    price = models.PositiveIntegerField(null=True)

    def __str__(self):
       return self.name

# Pizza base Class
class PizzaBase(models.Model):
    class Meta:
        verbose_name = "Pizza Base"
        verbose_name_plural = "Pizzas Base"

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    image = models.FileField(upload_to='upload/', blank=True, null=True)
    aditions = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

# Pizza Class
class Pizza(models.Model):
    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

    SMALL = 'SM'
    MEDIUM = 'MD'
    LARGE = 'LG'
    EXTRA_LARGE = 'XL'

    PIZZA_SIZE_CHOICES = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (EXTRA_LARGE, 'Extra Large')
    )

    pizza_base = models.ForeignKey(PizzaBase)
    price = models.PositiveIntegerField(null=True)
    size = models.CharField(
        max_length=2,
        choices=PIZZA_SIZE_CHOICES,
        default=LARGE,
    )

# Sale Class
class Sale(models.Model):
    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = "Sales"

    PENDING = 'PE'
    DONE = 'DO'
    
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DONE, 'Done')
    )
    
    salesman = models.ForeignKey(Employee)
    client = models.ForeignKey(Client)
    pizza = models.ManyToManyField(Pizza)
    date = models.DateTimeField()
    type = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
