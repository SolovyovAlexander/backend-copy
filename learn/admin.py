from django.contrib import admin

from .models import *


# Register your models here.
class SectionAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class LessonAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description', 'section')


admin.site.register(Section, SectionAdmin)
admin.site.register(Lesson, LessonAdmin)
