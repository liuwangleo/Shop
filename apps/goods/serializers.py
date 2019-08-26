from rest_framework import serializers
from goods.models import Goods, GoodsCategory


'''
drf的Modelserializer实现商品列表页
'''
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'

