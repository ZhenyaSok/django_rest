from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):
    """Мой базовый пагинатор"""

    page_size = 2  # Количество элементов на странице
    page_size_query_param = (
        "page_size"
    )
    max_page_size = 10  # Максимальное количество элементов на странице