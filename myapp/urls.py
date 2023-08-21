from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.detail, name='detail'),
    path('createproduct/',views.create_product, name='createproduct'),
]