from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'


urlpatterns = [
    path('',views.index,name="index"),
    path('post/<str:url>',views.detail, name="detail"),
    path("new_something_url", views.new_url_view, name="new_page_url" ),
    path("old_url", views.old_url_redirect, name="old_url" ),
    path("about", views.about_view, name="about" ),
     path("contact", views.contact_view, name="contact" ),
]
