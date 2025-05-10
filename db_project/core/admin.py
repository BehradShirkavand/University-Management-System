from django.contrib import admin
from . import models


admin.site.register(models.Classroom)
admin.site.register(models.Department)
admin.site.register(models.Course)
admin.site.register(models.Instructor)
admin.site.register(models.Section)
admin.site.register(models.Teaches)
admin.site.register(models.Student)
admin.site.register(models.Takes)
admin.site.register(models.Advisor)
admin.site.register(models.TimeSlot)
admin.site.register(models.Prereq)