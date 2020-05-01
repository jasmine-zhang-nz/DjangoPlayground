from django.shortcuts import render
from Item.models import Item


def index(request):
    items = Item.objects
    return render(request, 'index.html', {'items': items})