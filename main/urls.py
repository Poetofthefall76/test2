from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.ProfileView.as_view(), name="profile-view'"),
    path("product/", views.ProductView.as_view(), name="product-view"),
    path('notification/', views.NotificationView.as_view(), name='notification'),
]