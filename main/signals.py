from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Group, Teacher, Student, StudentMark


@receiver(post_save, sender=Group)
def group_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f" Группа '{instance.name}' успешно создана! ")


@receiver(post_save, sender=Teacher)
def teacher_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Преподаватель '{instance.name}' успешно добавлен!")


@receiver(post_save, sender=Student)
def student_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Студент '{instance.full_name}' успешно добавлен!")


@receiver(post_save, sender=StudentMark)
def mark_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Оценка поставлена: {instance.student} -> {instance.mark}")