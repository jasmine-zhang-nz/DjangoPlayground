from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.


def singleItem(request, item_id):

    singleOb = get_object_or_404(Item, pk=item_id)
    render(request, "singleItemPage.html", {'single_item': singleOb})
