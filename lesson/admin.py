from django.contrib import admin
from lesson.models import Lesson, LessonStatus


@admin.register(LessonStatus)
class LessonStatusAdmin(admin.ModelAdmin):
    list_display = ('id_lesson', 'id_user', 'time_view', 'get_status')

    def get_status(self, obj):
        return obj.status

    get_status.short_description = "status"


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'duration')
