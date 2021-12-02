from .models import Category, SubCategory
from .serializers import SubCategoriesSerializer
from django.shortcuts import render
from django.views.generic.edit import View
from rest_framework import generics


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
