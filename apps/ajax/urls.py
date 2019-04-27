from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('subcategories/', SubCategories.as_view(), name='subcategories'),
    path('subcategories/<int:parent>/', SubCategories.as_view(), name='subcategories-filtered'),
]
