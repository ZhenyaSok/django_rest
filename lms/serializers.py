from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.relations import SlugRelatedField

from lms.models import Course, Subject, Subscribe
from lms.validators import validator_scam_url



class CourseListSerializer(serializers.ModelSerializer):
    quantity_subject = serializers.SerializerMethodField()
    list_subject = serializers.SerializerMethodField()
    is_subscription = serializers.SerializerMethodField()

    def get_is_subscription(self, course):
        user = self.context['request'].user
        subscription = Subscribe.objects.filter(course=course.id, user=user.id)
        if subscription:
            return True
        return False

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
    link = serializers.URLField(validators=[validator_scam_url])
    class Meta:
        model = Subject
        fields = ('id', 'title', 'description', 'link', 'course')


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('id', 'user', 'course')

