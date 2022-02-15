from django.urls import path
from .views import home_view


app_name = 'shop'
urlpatterns = [
    path('', home_view),
]