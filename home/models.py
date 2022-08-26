
from django.db import models

from wagtail.core.models import Page
from wagtail.search.models import Query

from modelcluster.fields import ParentalKey
from django import forms
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.core.paginator import Paginator


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)

        context['products'] = Product.objects.child_of(self).live()[:6]

        return context


class Product(Page):
    def get_context(self, request):
        context = super().get_context(request)
        fields = []
        for f in self.custom_fields.get_object_list():
            if f.options:
                f.options_array = f.options.split('|')
                fields.append(f)
            else:
                fields.append(f)

        context['custom_fields'] = fields

        return context
    sku = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('sku'),
        FieldPanel('price'),
        ImageChooserPanel('image'),
        FieldPanel('short_description'),
        InlinePanel('custom_fields', label='Custom fields'),
    ]


SIZE_CHOICES = [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL')
]


class ProductCustomField(Orderable):
    product = ParentalKey(Product, on_delete=models.CASCADE,
                          related_name='custom_fields')
    name = models.CharField(max_length=255)
    options = models.CharField(
        max_length=500, choices=SIZE_CHOICES, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('options')
    ]


def shop(request):
    products = Product.objects.live()
    p = Paginator(products, 10)
    # shows number of items in page
    totalProducts = (p.count)
    pageNum = request.GET.get('page', 1)
    page1 = p.page(pageNum)

    return TemplateResponse(request, 'home/shop.html', {
        'products': products,
        'dataSaved': page1
    })


def about(request):
    return TemplateResponse(request, 'home/about.html', {
    })


def contact(request):
    return TemplateResponse(request, 'home/contact.html', {
    })


@register_setting
class SnipcartSettings(BaseSetting):
    api_key = models.CharField(
        max_length=255,
        help_text='Your Snipcart public API key'
    )


"""
def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()
    return TemplateResponse(request, 'home/search.html', {
    })
"""


def search(request):
    if request.method == "POST":
        searched = request.POST('searched')
        return TemplateResponse(
            request,
            "home/search.html",
            {'searched': searched}
        )
    else:
        return TemplateResponse(
            request,
            "home/search.html",
            {'searched': searched}
        )