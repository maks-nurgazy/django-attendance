from django.contrib import admin
from .models import Teacher, Course, Student, Fingerprint, Attendance, Record

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Fingerprint)
admin.site.register(Attendance)
admin.site.register(Record)
