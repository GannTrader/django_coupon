from django.urls import path
from .import views
app_name = 'sales'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add-to-cart/<int:id>', views.add_to_cart, name = 'add-to-cart'),
    path('view-cart/', views.view_cart, name = 'view-cart'),
    path('payment/', views.payment, name = 'payment'),
]