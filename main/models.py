from django.db. models import Model
from django.db import models

# Create your models here.

class Student(Model):
    avatar = models.ImageField(verbose_name="Аватарка: ", null=True, blank=True)
    first_name = models.CharField(max_length=300, verbose_name="Имя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия", blank=True, null=True)
    age = models.IntegerField(verbose_name="Возраст", blank=True, null=True)
    phone_numbers = models.CharField(max_length=20, verbose_name="Номер телефона")
    parent_phone_numbers = models.CharField(max_length=20, verbose_name="Номер телефона родителей", 
                                            blank=True, null=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, 
                              verbose_name= "Группа")




    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
class StudentMark(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name="Студент")
    mark = models.IntegerField(verbose_name="Оценка")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}: {self.mark}"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"


class Group(Model):
    name = models.CharField(max_length=100, verbose_name="Названия группы")
    start_date = models.DateField(verbose_name='Дата начнла')
    end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    course = models.CharField(max_length=100, verbose_name="Курс")
    student_count = models.IntegerField(verbose_name="Каличество учеников")
    contract = models.CharField(max_length=100, verbose_name="Контракт", default=8000)
    mentor = models.ForeignKey('Teacher', on_delete=models.SET_NULL, verbose_name='Ментор',
                               null=True, blank=True, related_name='groups')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    DIRECTION_CHOICES = (
        ("be", "Back-end"),
        ("fe", "Front-end"),
        ("smm", "SMM")
    )
    director = models.CharField(
        max_length=100, 
        verbose_name='Направление', 
        choices=DIRECTION_CHOICES
    )
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", blank=True, null=True)
    experience = models.IntegerField(default=0, verbose_name="Опыт работы (лет)")

    def __str__(self):
        return f"{self.name} ({self.get_director_display()})"
        return self.name

    
    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

