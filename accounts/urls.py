from django.urls import path
from .views import login, logout, register_user, getUsers, delete_user, update_user, add_user

urlpatterns= [
    path('login/', login, name='login'),
    path('register_patient/', register_user, name='register_patient'),
    path('logout/', logout, name='logout'),
    path('users/', getUsers, name='users'),
    path('deleteuser/<int:user_id>', delete_user, name ='deleteuser'),
    path('updateuser/<int:user_id>', update_user, name ='updateuser'),
    path('createuser', add_user, name ='createuser')
]