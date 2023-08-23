from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.detail, name='detail'),
    path('createproduct/',views.create_product, name='createproduct'),
    path('editproduct/<int:id>/',views.product_edit, name='editproduct'),
    path('delete/<int:id>/',views.product_delete,name='delete'),
    path('dashboard', views.dashboard, name='dashboard'),
]