from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, generics

from lms.models import Course, Subject
from lms.serializers import CourseSerializer, SubjectSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class SubjectCreateApiView(generics.CreateAPIView):
    serializer_class = SubjectSerializer


class SubjectListApiView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class SubjectRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class SubjectUpdateApiView(generics.UpdateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectDeleteApiView(generics.DestroyAPIView):
    queryset = Subject.objects.all()






