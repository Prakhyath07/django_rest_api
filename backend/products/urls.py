from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductCreateAPIView.as_view(), name='product_create_and_view'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product_detail_view'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product_update'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view(), name='product_delete'),


]
