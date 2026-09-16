from django.urls import path

from .views import * 


app_name = 'main'

urlpatterns = [
    path("", main_view, name="asosiy"),
    path('add-post/', create_post,  name='create_post'),
    path('delete-post/', delete_post, name="delete"),
    path("toggle-task/", toggle_task_status, name="task_done"),
    path("login/", login_view, name="login_page"),
    path("logout/", logout_view , name="logout")
]