from django.contrib import admin
from lms.models import Subject, Course
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

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Отображение списка платежей"""
    list_display = ('user_pay', 'date_pay', 'paid_course', 'paid_subject')



