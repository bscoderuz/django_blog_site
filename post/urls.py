from django.urls import path
from .views import home, about, post_detail

urlpatterns = [
    path('', home, name="blog-home"),
    path('about/', about, name="blog-about"),
    path('post/<int:id>/', post_detail, name="blog-detail"),
]
