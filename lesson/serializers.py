from rest_framework import serializers


class LessonStatusSerializer(serializers.Serializer):
    lesson_name = serializers.CharField(source='id_lesson__name')
    view_time = serializers.IntegerField(source='time_view')
    view_status = serializers.CharField(source='view_status_word')


class ProductLessonStatusSerializer(serializers.Serializer):
    lesson_name = serializers.CharField(source='id_lesson__name')
    view_time = serializers.IntegerField(source='time_view')
    view_status = serializers.CharField(source='view_status_word')
    view_date = serializers.DateField()
