
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from config import settings
from users.models import User, Payment
import stripe
from lms.permissions import IsOwner, IsModerator
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_price, create_stripe_session

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
        print(course)

        if not course:
            raise serializers.ValidationError('Укажите курс')
        payment = serializer.save()

        if course.price != payment.payment_summ:
            raise serializers.ValidationError('Укажите верную цену, должна совпадать с ценой на сайте')

        stripe_price_id = create_stripe_price(payment)
        print(f"PRICE-id{stripe_price_id}")
        payment.payment_link = create_stripe_session(stripe_price_id)
        # print(f"LINK{payment.payment_link}")
        # payment.payment_link.rstrip('/').split('/')[-1].split('-')[0]

        # payment.save()



#     def post(self, request, *args, **kwargs):
#         super(PaymentCreateAPIView, self).post(request, *args, **kwargs)
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     'price': 'price_1OzDyORoEJdjRqgtewTvrPqW',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=settings.DOMAIN_NAME,
#             cancel_url='http://127.0.0.1:8000/payment/'
# ,
#         )
#         return HTTPResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)


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




