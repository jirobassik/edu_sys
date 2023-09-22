from datetime import date

from django.db import models
from user.models import User


class Lesson(models.Model):
    name = models.CharField("Lesson name", max_length=100, null=False, blank=False, unique=True)
    link = models.URLField("Link to lesson", null=False, blank=False)
    duration = models.PositiveBigIntegerField("Video duration", null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class LessonStatus(models.Model):
    id_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_view = models.PositiveBigIntegerField("View time", null=False, blank=False, default=0)
    view_status = models.BooleanField(editable=False, auto_created=True, default=False)
    view_date = models.DateField(editable=False, default=date.today)

    def save(self, *args, **kwargs):
        self.view_status = bool((self.time_view / self.id_lesson.duration) * 100 > 80)
        super().save(*args, **kwargs)

    @property
    def status(self):
        return "Просмотрено" if (self.time_view / self.id_lesson.duration) * 100 > 80 else "Не просмотрено"

    def __str__(self):
        return f"lesson {self.id_lesson.name} status for user {self.id_user.surname}"
