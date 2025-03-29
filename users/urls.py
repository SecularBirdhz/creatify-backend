from django.urls import path
from .views import SignupView, SigninView, MeView

app_name = 'users'  # 命名空间标识

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('me/', MeView.as_view(), name='me'),
]