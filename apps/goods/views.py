from rest_framework import generics, mixins, viewsets

from goods.models import Goods
from goods.serializers import GoodsSerializer
from rest_framework.pagination import PageNumberPagination


class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 2
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


# class GoodsListView(generics.ListAPIView):
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    商品列表页
    '''
    pagination_class = GoodsPagination  # 分页
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
