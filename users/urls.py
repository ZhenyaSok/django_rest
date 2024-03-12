from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_new_password, \
    UserConfirmEmailView, UserConfirmView, UserConfirmFailView, UserConfirmSentView, PaymentListApiView

app_name = UsersConfig.name





urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),

    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email_confirmed/', UserConfirmView.as_view(), name='email_confirmed'),
    path('email_info_failed/', UserConfirmFailView.as_view(), name='email_info_failed'),
    path('email_senting/', UserConfirmSentView.as_view(), name='email_senting'),

    path('payment/', PaymentListApiView.as_view(), name='payment'),

]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]