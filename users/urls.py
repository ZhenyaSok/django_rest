from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PaymentListApiView, UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView, \
    UserRetrieveAPIView, PaymentCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = UsersConfig.name


urlpatterns = [

    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('list/', UserListAPIView.as_view(), name='list'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', UserDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='detail'),

    path('payment/', PaymentListApiView.as_view(), name='payment'),
    path('payment_create/', PaymentCreateAPIView.as_view(), name='payment_create'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
