from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-item'),
    path('booking/', views.BookingView.as_view(), name='booking'),
]
