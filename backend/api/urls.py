from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView, SendMessage, CheckMessage

urlpatterns = [
    path('auth/login/',obtain_auth_token,name='auth_user_login'),
    path('auth/register/',CreateUserAPIView.as_view(), name='auth_user_create'),
    path('auth/logout/', LogoutUserAPIView.as_view(),name='auth_user_logout'),
    path('auth/send/', SendMessage.as_view(), name="auth_sms_send"),  
    path('auth/check/', CheckMessage.as_view(), name="auth_sms_check")    

]
