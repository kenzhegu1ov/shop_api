from django.urls import include, path
from django.contrib import admin
from product.views import (
    category_list,
    category_detail,
    product_list,
    product_detail,
    review_list,
    review_detail,
    product_reviews

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', category_list, name='category-list'),
    path('api/v1/categories/<int:id>/', category_detail, name='category-detail'),
    path('api/v1/products/', product_list, name='product-list'),
    path('api/v1/products/<int:id>/', product_detail, name='product-detail'),
    path('api/v1/reviews/', review_list, name='review-list'),
    path('api/v1/reviews/<int:id>/', review_detail, name='review-detail'),
    path('api/v1/products/reviews/', product_reviews, name='product-reviews'),
]
