from django.contrib import admin
from ims.models import Subject, Course


@admin.register(Subject)
class SubjectListSettingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'course', 'owner',)
    list_filter = ('title',)
    search_fields = ('title', 'pk',)

@admin.register(Course)
class CourseListSettingsAdmin(admin.ModelAdmin):
    # list_filter = ('title', 'course')
    list_display = ('pk', 'title', 'description', 'owner', )


# Register your models here.
