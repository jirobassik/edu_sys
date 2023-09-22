from django.db import models
from lesson.models import Lesson
from user.models import User


class Product(models.Model):
    name = models.CharField("Product name", max_length=100, null=False, blank=False)
    owner = models.CharField("Owner name", max_length=30, null=False, blank=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    access_product = models.ManyToManyField(User)  # Может вынести в отдельную таблицу

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
