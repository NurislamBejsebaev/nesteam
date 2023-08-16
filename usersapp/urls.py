from django.urls import path
from usersapp.views import *

urlpatterns = [
    path('list/', UsersList.as_view(), name='user-list'),
    path('detail/<int:pk>/', UsersDetail.as_view(), name='user-detail'),
]
