from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, generics
from lms.models import Course, Subject, Subscribe
from lms.permissions import IsModerator, IsOwner
from lms.serializers import CourseListSerializer, SubjectSerializer, SubscribeSerializer


class SubscribeViewSet(ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

    def post(self, *args, **kwargs):
        '''
        def post(self, *args, **kwargs):
    user = получаем пользователя из self.requests
    course_id = получаем id курса из self.reqests.data
    course_item = получаем объект курса из базы с помощью get_object_or_404

    subs_item = получаем объекты подписок по текущему пользователю и курса

		# Если подписка у пользователя на этот курс есть - удаляем ее
    if subs_item.exists():
        ...
        message = 'подписка удалена'
		# Если подписки у пользователя на этот курс нет - создаем ее
    else:
        ...
        message = 'подписка добавлена'
		# Возвращаем ответ в API
    return Response({"message": message})
        '''
        pass


class CourseViewSet(ModelViewSet):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve' or 'update' or 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner|IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

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
    # permission_classes = [IsAuthenticated, IsOwner|IsModerator]

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











