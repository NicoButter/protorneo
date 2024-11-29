from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:home'), name='logout'),
]
