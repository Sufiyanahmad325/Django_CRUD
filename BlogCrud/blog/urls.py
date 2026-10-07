from django.urls import path
from . import views



urlpatterns=[
    path('register/',views.register_view,name='register'),
    path('login/' , views.login_view , name='login'),
    path('home/' , views.home_view , name='home'),
    path("create-blog/", views.create_blog_view, name="create_blog"),
]