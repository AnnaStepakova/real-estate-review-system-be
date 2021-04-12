from django.conf import settings

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = settings.REST_FRAMEWORK.get('PAGE_SIZE')
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'items_count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'page_number': self.page.number,
            'results': data
        })
