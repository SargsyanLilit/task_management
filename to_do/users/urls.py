from django.urls import path, include
from users import views


urlpatterns = [
    path('create-user/', views.create_user, name='create'),
    path('user-profile/', views.profile, name='user-profile'),
    path('user-login/', views.user_login, name='user-login'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('user-update/', views.user_update, name='user-update'),

]
