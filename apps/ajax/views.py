from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import SubCategoriesSerializer
from django.views.generic.edit import View


# Create your views here.
class SubCategories(generics.ListAPIView):
    serializer_class = SubCategoriesSerializer

    def get_queryset(self):
        if 'parent' in self.kwargs:
            return SubCategory.objects.filter(parent=self.kwargs['parent'])
        return SubCategory.objects.all()


class Index(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        subcategories = SubCategory.objects.filter(parent=categories[0])
        return render(request, 'ajax/index.html', {'categories': categories, 'subcategories': subcategories})
