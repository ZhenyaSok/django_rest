from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, generics
from lms.models import Course, Subject, Subscribe
from lms.pagination import PagePagination
from lms.permissions import IsModerator, IsOwner
from lms.serializers import SubjectSerializer, CourseSerializer


# class SubscribeViewSet(ModelViewSet):
#     serializer_class = SubscribeSerializer
#     queryset = Subscribe.objects.all()

class SubscribeAPIView(APIView):
    """Механизм для смены флага подписки на курс"""

    def post(self, request, *args, **kwargs):
        """Реализация задания через post метод"""
        user = request.user
        course_id = request.data.get("course_id")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Subscribe.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        else:
            Subscribe.objects.create(user=user, course=course_item)
            message = "Подписка добавлена"

        return Response({"message": message}, status=status.HTTP_200_OK)

class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = PagePagination

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [~IsModerator, IsAuthenticated]
        elif self.action == 'retrieve' or 'list':
            permission_classes = [IsModerator | IsOwner]
        elif self.action == 'update' or 'partial_update':
            permission_classes = [IsModerator | IsOwner]
        elif self.action == 'destroy':
            permission_classes = [~IsModerator, IsOwner]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

class SubjectCreateApiView(generics.CreateAPIView):
    serializer_class = SubjectSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_subject = serializer.save()
        new_subject.owner = self.request.user
        new_subject.save()

class SubjectListApiView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    pagination_class = PagePagination
    # permission_classes = [IsAuthenticated, IsOwner|IsModerator]

class SubjectRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner|IsModerator]

class SubjectUpdateApiView(generics.UpdateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner|IsModerator]

class SubjectDeleteApiView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]











