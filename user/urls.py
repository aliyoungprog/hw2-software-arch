from django.urls import path
from .views import get_all, add_user, update_user, delete_user

urlpatterns = [
    path('', get_all, name="list_users"),
    path('new', add_user, name='create_users'),
    path('update/<int:id>', update_user, name='update_user'),
    path('delete/<int:id>', delete_user, name='delete_user')
]

