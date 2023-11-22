from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Services(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}: {self.title}/n"

    @classmethod
    def search_services(cls, query):
        """
        Method to search for services based on a query.
        """
        return cls.objects.filter(title__icontains=query)



