from rest_framework import serializers

from learn.models import Section, Lesson, LessonLike


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    section = SectionSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'


class ImageLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['image']


class LessonLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonLike
        fields = '__all__'
