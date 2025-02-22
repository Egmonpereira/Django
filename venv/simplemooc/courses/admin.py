from django.contrib import admin

# Register your models here.
from .models import (
    Course, Enrollment, Announcement, Comment, Lesson, Material
)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MatrialInlineAdmin(admin.StackedInline):
#class MatrialInlineAdmin(admin.TabularInline):
    
    model = Material

class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

    inlines = [
        MatrialInlineAdmin
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)