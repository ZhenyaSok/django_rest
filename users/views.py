from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from config import settings
from users.models import User, Payment
import stripe
from lms.permissions import IsOwner, IsModerator
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_price, create_stripe_session, get_status_payment

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentListApiView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('date_pay', 'paid_subject', 'paid_course', 'payment_method')
    ordering_fields = ('date_pay',)
    # permission_classes = [IsAuthenticated]



class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        course = serializer.validated_data.get('paid_course')

        if not course:
            raise serializers.ValidationError('Укажите курс')
        payment = serializer.save()

        if course.price != payment.payment_summ:
            raise serializers.ValidationError('Укажите верную цену, должна совпадать с ценой на сайте')

        stripe_price_id = create_stripe_price(payment)
        payment.payment_link, payment.payment_id = create_stripe_session(stripe_price_id)

        get_status_payment(payment.payment_id)

        payment.save()


class StatusViewSet(ModelViewSet):
    queryset = Payment.objects.all()


    def retrieve(self, request, pk):

        instance = pk
        serializer = PaymentSerializer(instance)
        return Response(serializer.data)
        # Метод для вывода информации по пользователю с определением выборки из базы и указанием сериализатора
        # queryset = Payment.objects.all()
        # payment_pk = stripe.checkout.Session.retrieve(queryset, pk=pk)
        # payment = get_object_or_404(queryset, pk=pk)

        # return Response(serializer.data)




    # payment_status = stripe.checkout.Session.retrieve(
    #     "cs_test_a1nY8SsGNE4yP7F0OI7skSKtc5ImzuHC6mQu7e1Hlh0ql1tvoEYikQTRsD")
    #
    # print(payment_status)

    # def get(self, request, *args, **kwargs):
    #     """Возвращает статус платежа"""
    #     s = request.data.get("course_id")
    #     print(s)




        # payment_status = stripe.checkout.Session.retrieve(payment.payment_id)
        # print(payment_status)


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner|IsModerator]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner|IsModerator]




