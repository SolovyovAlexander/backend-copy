from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from users.models import User


class Section(models.Model):
    name = models.CharField(_('name'), max_length=256)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(_('name'), max_length=256)
    description = models.TextField(_('description'))
    link = models.URLField(_('link'))
    image = models.ImageField(_('image'), blank=True, null=True)
    section = models.ForeignKey(Section, models.CASCADE, verbose_name=_('section'))

    def __str__(self):
        return self.name


class LessonLike(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('user'))
    lesson = models.ForeignKey(Lesson, models.CASCADE, verbose_name=_('lesson'))
    timestamp = models.TimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'lesson']
