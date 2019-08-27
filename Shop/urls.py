"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

import xadmin
from django.views.static import serve

from Shop.settings import MEDIA_ROOT
# from goods.views_base import GoodsListView
# from goods.views import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='融合API')
router = routers.DefaultRouter()
router.register(r'goods', GoodsListViewSet, base_name='goods')
router.register(r'categorys', CategoryViewSet, base_name='categorys')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # path('docs', include_docs_urls(title='文档')),
    path('docs/', schema_view),
    path('api-auth/', include('rest_framework.urls')),

    # 商品
    # path('goods/', GoodsListView.as_view(), name='goods_list'),
    # re_path('^', include(router.urls)),
    path('api/', include(router.urls)),
]
