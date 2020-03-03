from datetime import date

from django.db import models


class Teacher(models.Model):
    firstName = models.CharField("Имя", max_length=50)
    lastName = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Course(models.Model):
    code = models.CharField("Код урока", max_length=15)
    name = models.CharField("Название урока", max_length=50)
    teacher = models.ForeignKey(Teacher, verbose_name="Инструктор", related_name="teachers_course",
                                on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Student(models.Model):
    rollNumber = models.CharField("ID студента", max_length=15)
    firstName = models.CharField("Имя", max_length=50)
    lastName = models.CharField("Фамилия", max_length=50)
    course = models.ManyToManyField(Course, verbose_name="Курсы", related_name="course_student")

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Fingerprint(models.Model):
    samples = models.ImageField("Отпечаток", upload_to="fingerprints/")
    student = models.ForeignKey(Student, verbose_name="Студент", on_delete=models.CASCADE)


class Attendance(models.Model):
    date = models.DateField("Дата", default=date.today)
    course = models.ForeignKey(Course, verbose_name="названия урока", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.course} - {self.date}"


class Record(models.Model):
    student = models.ForeignKey(Student, verbose_name="Студент", on_delete=models.CASCADE)
    status = models.BooleanField("Статус", default=True)
    attendance = models.ForeignKey(Attendance, verbose_name="посещаемость", on_delete=models.CASCADE)
