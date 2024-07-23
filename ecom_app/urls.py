from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='ecom'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('furniture/', views.furniture, name='furniture'),
    path('interior/', views.interior, name='interior'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('contact/', views.contact, name='contact'),

    # furnitures
    path('product/<str:cat_id>/', views.product, name='product'),
    path('product/<str:cat_id>/<int:single_id>/', views.detail, name='detail'),




    # interiors
    #path('home/interior/bathroom/', views.bathroom, name='bathroom'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)