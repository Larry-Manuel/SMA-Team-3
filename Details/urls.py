from django.urls import path
from. import views

# api_name = "details"
app_name = "Details"
urlpatterns = [
    path("create_post/", views.create_post, name="create_post"),
    path("update_post/<int:id>/", views.update_post, name="update_post"),
    path("delete_post/<int:id>/", views.delete_post, name="delete_post"),
    path('like_post/<post_id>/', views.like_post, name='like_post'),
    path('unlike_post/<post_id>/', views.unlike_post, name='unlike_post'),
    path('send_message/', views.send_message, name='send_message'),
    path('send_user_message/<int:id>', views.send_user_message, name='send_user_message'),
]



