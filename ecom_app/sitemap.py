from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from ecom_app.models import Category, SubCategory, Products

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

    def changefreq(self, obj):
        return obj.changefreq

    def priority(self, obj):
        return obj.priority


class SubCategorySitemap(Sitemap):
    def items(self):
        return SubCategory.objects.all()

    def changefreq(self, obj):
        return obj.changefreq

    def priority(self, obj):
        return obj.priority


class ProductsSitemap(Sitemap):
    def items(self):
        return Products.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def changefreq(self, obj):
        return obj.changefreq

    def priority(self, obj):
        return obj.priority