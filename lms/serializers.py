from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.relations import SlugRelatedField

from lms.models import Course, Subject


class CourseListSerializer(serializers.ModelSerializer):
    quantity_subject = serializers.SerializerMethodField()
    list_subject = serializers.SerializerMethodField()

    def get_quantity_subject(self, course):
        """Метод для подсчета количества уроков, входящих в курс"""
        return Subject.objects.filter(course=course).count()


    def get_list_subject(self, course):
        """Метод выводит все уроки в курсе"""
        return [subject.title for subject in Subject.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = ("title", "list_subject", "description", "quantity_subject")



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'