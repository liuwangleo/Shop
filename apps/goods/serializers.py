from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsImage

'''
drf的Modelserializer实现商品列表页
'''


class CategorySerilizer3(serializers.ModelSerializer):
    '''
    三级级分类
    '''

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerilizer2(serializers.ModelSerializer):
    '''
    二级分类
    '''
    sub_cat = CategorySerilizer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    '''
    商品一级类别
    '''
    sub_cat = CategorySerilizer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'


class GoodsImageSerializer(serializers.ModelSerializer):
    image = GoodsSerializer()

    class Meta:
        model = GoodsImage
        fields = "__all__"
