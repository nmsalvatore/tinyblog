from django.urls import path
from .views import post_list_view, post_detail_view, post_new_view, post_edit_view, post_delete_view

urlpatterns = [
    path("<str:path>/", post_list_view, name="post_list"),
    path("<str:path>/<str:slug>/", post_detail_view, name="post_detail"),
    path("<str:path>/post/new/", post_new_view, name="post_new"),
    path("<str:path>/post/edit/<str:slug>/", post_edit_view, name="post_edit"),
    path("<str:path>/post/delete/<str:slug>/", post_delete_view, name="post_delete"),
]
