from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify_account/<str:token>', views.verify_account, name='verify_account'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<str:token>', views.reset_password, name='reset_password'),
]