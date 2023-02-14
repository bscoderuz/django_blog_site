from django.urls import path
from .views import home, about, post_detail, post_create

urlpatterns = [
    path('', home, name="blog-home"),
    path('about/', about, name="blog-about"),
    path('post/<int:id>/', post_detail, name="blog-detail"),
    path('create-post/', post_create, name="new-blog"),
]
