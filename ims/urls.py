from django.urls import path

from ims.apps import ImsConfig
from rest_framework.routers import DefaultRouter

from ims.views import CourseViewSet, SubjectCreateApiView, SubjectListApiView, SubjectRetrieveApiView, \
    SubjectUpdateApiView, SubjectDeleteApiView

app_name = ImsConfig.name

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')

urlpatterns = [
    path('subject/create/', SubjectCreateApiView.as_view(), name='subject_create'),
    path('subject/list/', SubjectListApiView.as_view(), name='subject_list'),
    path('subject/<int:pk>/', SubjectRetrieveApiView.as_view(), name='subject_get'),
    path('subject/update/<int:pk>', SubjectUpdateApiView.as_view(), name='subject_update'),
    path('subject/delete/<int:pk>', SubjectDeleteApiView.as_view(), name='subject_delete'),
] + router.urls