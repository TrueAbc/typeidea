from rest_framework import viewsets
# from rest_framework.permissions import IsAdminUser

from .models import Post, Category
from .serializer import (
    PostSerializer, PostDetailSerializer,
    CategorySerializer, CategoryDetailSerializer, 
)


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    # 具有CRUD功能的模型是modeliewset
    ''' 提供文章的接口 '''
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    # permission_classes = [IsAdminUser]  # 写入时的权限校验
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super(PostViewSet, self).retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super(CategoryViewSet, self).retrieve(request, *args, **kwargs)