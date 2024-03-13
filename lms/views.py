from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, generics
from lms.models import Course, Subject
from lms.permissions import IsModerator, IsOwner
from lms.serializers import CourseListSerializer, SubjectSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action ==  'retrieve' or 'update' or 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner|IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class SubjectCreateApiView(generics.CreateAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_subject = serializer.save()
        new_subject.owner = self.request.user
        new_subject.save()

class SubjectListApiView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsOwner|IsModerator]

class SubjectRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsOwner|IsModerator]

class SubjectUpdateApiView(generics.UpdateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsOwner|IsModerator]

class SubjectDeleteApiView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]











