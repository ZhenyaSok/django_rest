from rest_framework import serializers

from users.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    user_pay = serializers.SlugRelatedField(slug_field='email', queryset=Payment.objects.all())
    paid_course = serializers.SlugRelatedField(slug_field='title', read_only=True)
    paid_subject = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Payment
        fields = ('id', 'user_pay', 'date_pay', 'paid_course', 'paid_subject', 'payment', 'payment_method')


