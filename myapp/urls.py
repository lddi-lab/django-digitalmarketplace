from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.detail, name='detail'),
    path('createproduct/',views.create_product, name='createproduct'),
    path('editproduct/<int:id>/',views.product_edit, name='editproduct'),
    path('delete/<int:id>/',views.product_delete,name='delete'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='myapp/login.html'), name='login'),
]