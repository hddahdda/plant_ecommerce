from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<item_id>', views.add_to_cart, name="add_to_cart"),
    path('adjust/<item_id>', views.adjust_cart, name="adjust_cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
