from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class CatalogView(View):
    def get(self, request):
        return render(request, 'catalog/catalog.html', context={'name': "RED"})