from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from ecom_app.sitemap import ProductsSitemap, SubCategorySitemap, CategorySitemap
sitemaps = {
    'sub_category' : SubCategorySitemap,
    'products': ProductsSitemap,
    'category' : CategorySitemap,
}
urlpatterns = [
    path('', include('ecom_app.urls')),
    path('admin/', admin.site.urls),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)