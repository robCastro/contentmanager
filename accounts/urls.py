from django.urls import path, include
from accounts import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', logout_then_login, name='logout'),
]
