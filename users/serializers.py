from rest_framework import serializers

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    # user_pay = serializers.SlugRelatedField(slug_field='email', queryset=Payment.objects.all())
    # paid_course = serializers.SlugRelatedField(slug_field='title', read_only=True)
    # paid_subject = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Payment
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

