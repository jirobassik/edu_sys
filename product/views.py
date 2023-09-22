from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count, Sum
from rest_framework.views import APIView
from product.models import Product
from lesson.models import LessonStatus
from lesson.serializers import LessonStatusSerializer
from user.models import User


class ProductStatistic(APIView):
    serializer_class = LessonStatusSerializer

    def get(self, request):
        products = Product.objects.all()
        product_statistic = []
        all_users = User.objects.aggregate(all_users=Count('id'))
        all_users_value = all_users['all_users']
        for product in products:
            amount_view_lessons = LessonStatus.objects.filter(id_lesson__product=product, view_status=True).aggregate(
                num_users=Count('view_status'))
            time_spent = LessonStatus.objects.filter(id_lesson__product=product).aggregate(total_time=Sum('time_view'))
            count_users = Product.objects.filter(lesson__product=product).aggregate(count_user=Count('access_product'))
            count_users_value = count_users['count_user']
            product_statistic.append({
                'product_name': product.name,
                'total_time_spent': time_spent['total_time'],
                'amount_view_lessons': amount_view_lessons['num_users'],
                'count_users': count_users_value,
                'product_profit_percent': (count_users_value / all_users_value) * 100
            })
        return Response(product_statistic, status=status.HTTP_200_OK) if product_statistic else Response(
            status=status.HTTP_404_NOT_FOUND)
