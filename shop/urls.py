from django.urls import path
from .views import (
    home_view,
    product_view,
)


app_name = 'shop'
urlpatterns = [
    path('', home_view),
    path('product/<int:pk>/', product_view, name='product_view'),
]