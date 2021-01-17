
from rest_framework import permissions, viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import SAFE_METHODS


from firebase_auth.authentication import FirebaseAuthentication
from learn.models import Section, Lesson
from learn.serializers import SectionSerializer, LessonSerializer, ImageLessonSerializer


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAdminUser | ReadOnly]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAdminUser | ReadOnly]
    authentication_classes = [FirebaseAuthentication, SessionAuthentication]

    @action(methods=['PUT'],  detail=True, parser_classes=[MultiPartParser], serializer_class=ImageLessonSerializer)
    def image(self, request, *args, **kwargs):
        return super(LessonViewSet, self).update(request, request, *args, **kwargs)

