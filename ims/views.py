from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, generics

from ims.models import Course, Subject
from ims.serializers import CourseSerializer, SubjectSerializer


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






