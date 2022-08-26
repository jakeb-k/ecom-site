from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.template.response import TemplateResponse
from home.models import Product

from wagtail.models import Page
from wagtail.search.models import Query

"""
def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Product.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Product.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",

    )
"""


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(title__contains=searched)
        print(searched)
        return TemplateResponse(
            request,
            "home/search.html",
            {'searched': searched,
             'products': products}
        )
    else:
        return TemplateResponse(
            request,
            "home/search.html",
        )


def searchSports(request):

    topic = 'Sport'
    products = Product.objects.filter(short_description__contains=topic)

    return TemplateResponse(
        request,
        "home/sports.html",
        {'topic': topic,
         'products': products}
    )


def searchConstruc(request):

    topic = 'Construction'
    products = Product.objects.filter(short_description__contains=topic)

    return TemplateResponse(
        request,
        "home/construction.html",
        {'topic': topic,
         'products': products}
    )


def searchHousehold(request):

    topic = 'Household'
    products = Product.objects.filter(short_description__contains=topic)

    return TemplateResponse(
        request,
        "home/household.html",
        {'topic': topic,
         'products': products}
    )
