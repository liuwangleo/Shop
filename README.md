# 商品列表页
    ## django的view实现商品列表页
        '''from django.views.generic import View
        from goods.models import Goods
        class GoodsListView(View):
            def get(self,request):
            通过django的view实现商品列表页
            json_list = []
            #获取所有商品
            goods = Goods.objects.all()
            for good in goods:
                json_dict = {}
                #获取商品的每个字段，键值对形式
                json_dict['name'] = good.name
                json_dict['category'] = good.category.name
                json_dict['market_price'] = good.market_price
                json_list.append(json_dict)
            from django.http import HttpResponse
            import json
            #返回json，一定要指定类型content_type='application/json'
            return HttpResponse(json.dumps(json_list),content_type='application/json')'''
    ## django的serializer
        '''from django.views.generic import View
        from goods.models import Goods
        class GoodsListView(View):
            def get(self,request):
                #通过django的view实现商品列表页
                json_list = []
                #获取所有商品
                goods = Goods.objects.all()
                from django.forms.models import model_to_dict
                for good in goods:
                    json_dict = model_to_dict(good)
                    json_list.append(json_dict)
                from django.http import HttpResponse
                import json
                #返回json，一定要指定类型content_type='application/json'
                return HttpResponse(json.dumps(json_list),content_type='application/json')'''
        虽然可以很简单实现序列化，但是有几个缺点,字段序列化定死的，要想重组的话非常麻烦
        从上面截图可以看出来，images保存的是一个相对路径，我们还需要补全路径，而这些drf都可以帮助我们做到
        以上写了这么多只是为了引入django rest framework和简单介绍django的序列化用法，下面就是重点讲解django rest framework了
    ## APIview方式实现商品列表页
        from rest_framework.views import APIView
    ## drf的Modelserializer实现商品列表页
        ''' from rest_framework import serializers
        class CategorySerializer(serializers.ModelSerializer):
            class Meta:
                model = GoodsCategory
                fields = "__all__"
        class GoodsSerializer(serializers.ModelSerializer):
            //覆盖外键字段
            category = CategorySerializer()
            class Meta:
                model = Goods
                fields = '__all__' '''
    ## GenericView实现商品列表页
        ListAPIView继承自mixins.ListModelMixin,GenericAPIView
            1.GenericAPIView
                GenericAPIView ——> APIView ——> View
                用的时候需要定义queryset和serializer_class
                GenericAPIView里面默认为空
                queryset = None
                serializer_class = None
            2.ListModelMixin
                具有分页功能 from rest_framework.pagination import PageNumberPagination
    ## viewsets和router完成商品列表页

    ## 过滤
        


