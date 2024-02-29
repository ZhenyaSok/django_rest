from rest_framework import serializers

from ims.models import Course, Subject


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        field = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        field = '__all__'