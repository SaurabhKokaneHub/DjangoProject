from django.urls import path
from clothing import views
urlpatterns = [
    path('', views.fashion_view, name='clothing'),
]
