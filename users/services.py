from django.core.mail import send_mail
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
def create_stripe_price(payment):
    stripe_product = stripe.Product.create(
        name=payment.paid_course.title
    )

    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=int(payment.payment_summ)*100,
        product_data={"name": stripe_product['name']},
    )

    return stripe_price['id']


def create_stripe_session(stripe_price_id):
    stripe_session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{
            'price': stripe_price_id,
            'quantity': 1
        }],
        mode='payment',
    )

    return stripe_session['url']


def send_mail_password(new_password, email):

    send_mail(subject='Вы сменили пароль',
        message=f'Ваш пароль: {new_password}!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
              )

def send_mail_ready(email, current_site, activation_url):
        send_mail(subject='Почти готово!',
                message=f"Завершите регистрацию, перейдя по ссылке: http://{current_site}{activation_url}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )
