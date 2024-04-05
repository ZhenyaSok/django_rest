from django.contrib import admin
from lms.models import Subject, Course, Subscribe
from users.models import Payment


@admin.register(Subject)
class SubjectListSettingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'course',)
    list_filter = ('title',)
    search_fields = ('title', 'pk',)

@admin.register(Course)
class CourseListSettingsAdmin(admin.ModelAdmin):
    # list_filter = ('title', 'course')
    list_display = ('pk', 'title', 'description', 'owner')


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    # list_filter = ('title', 'course')
    list_display = ('pk', 'user', 'course', 'status_subscribe')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Отображение списка платежей"""
    list_display = ('id', 'user_pay', 'date_pay', 'payment_id', 'paid_course', 'paid_subject')



