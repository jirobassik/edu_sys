from rest_framework import status
from rest_framework.response import Response
from django.db.models import Case, When, Value, CharField
from rest_framework.views import APIView
from product.models import Product
from lesson.models import LessonStatus
from lesson.serializers import LessonStatusSerializer, ProductLessonStatusSerializer


def get_lesson_time_view(lessons_id, user_id, *args):
    return LessonStatus.objects.filter(id_lesson__in=lessons_id, id_user=user_id).prefetch_related(
        'id_lesson').annotate(
        view_status_word=Case(
            When(view_status=True, then=Value('Просмотрено')),
            When(view_status=False, then=Value('Не просмотрено')),
            default=Value('Unknown'),
            output_field=CharField()
        )
    ).values(*args)


class LessonsUserView(APIView):
    serializer_class = LessonStatusSerializer

    def get(self, request, pk):
        user_id = pk
        lessons_id = Product.objects.filter(access_product=user_id).values_list('lesson', flat=True)
        serializer = self.serializer_class(
            get_lesson_time_view(lessons_id, user_id, 'id_lesson__name', 'time_view', 'view_status_word'), many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK) if serialized_data else Response(
            status=status.HTTP_404_NOT_FOUND)


class ProductDetailLessonUserView(APIView):
    serializer_class = ProductLessonStatusSerializer

    def get(self, request, pk, product):
        product_name = product
        user_id = pk
        lessons_id = Product.objects.filter(access_product=user_id, name=product_name).values_list('lesson',
                                                                                                   flat=True)
        serializer = self.serializer_class(
            get_lesson_time_view(lessons_id, user_id, 'id_lesson__name', 'time_view', 'view_status_word', 'view_date'),
            many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK) if serialized_data else Response(
            status=status.HTTP_404_NOT_FOUND)
