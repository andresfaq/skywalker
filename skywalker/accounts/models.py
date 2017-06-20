"""
author: Bryan Tabarez
"""

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
    PermissionsMixin)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Standard fields: username, first_name, last_name, email
    # is_staff, is_active, is_superuser, last_login, date_joined
    # username = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now=True)

    # Additionar fields: address, date_of_birth, cellphone, dni, phone
    address = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    cellphone = models.PositiveIntegerField(blank=True, null=True)
    dni = models.PositiveIntegerField(blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email


class Employee(models.Model):
    ADMINISTRATOR = 'administrator'
    EMPLOYEE = 'employee'

    EMPLOYEE_TYPE_CHOICES = (
        (ADMINISTRATOR, 'Administrator'),
        (EMPLOYEE, 'Employee'),
    )

    salary = models.PositiveIntegerField(null=True)
    employee_type = models.CharField(
        max_length=15,
        choices=EMPLOYEE_TYPE_CHOICES,
        default=EMPLOYEE,
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
