from django.db import models


class User(models.Model):
    name = models.CharField("User name", max_length=100, blank=False, null=False)
    surname = models.CharField("User surname", max_length=100, blank=False, null=False)

    def __str__(self):
        return self.surname

    class Meta:
        ordering = ['surname']
