from django.urls import path
from .views import post_list_view, post_detail_view

urlpatterns = [
    path("<str:path>", post_list_view, name="post_list"),
    path("<str:path>/<str:slug>/", post_detail_view, name="post_detail"),
]
