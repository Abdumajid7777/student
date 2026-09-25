from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Group, Teacher, StudentMark
def index(request):
    q = request.GET.get('q', '').strip()
    
    groups = Group.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    marks = StudentMark.objects.all()
    
    return render(request, 'index.html', {
        'groups': groups,
        'students': students,
        'teachers': teachers,
        'marks': marks,
    })






# === Student ===

def student_index(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        students = Student.objects.all()

    students_count = students.count()

    return render(
        request,
        'student_index.html',
        {'students': students, 'students_count': students_count},
    )

def student_create(request):
    groups = Group.objects.all()

    if request.method == "POST":
        messages.success(request, "Студент успешно добавлен!")
        return redirect("student_index")

    return render(request, "student_create.html", {"groups": groups})

def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age') or None
        student.phone_numbers = request.POST.get('phone_numbers')
        student.parent_phone_numbers = request.POST.get('parent_phone_numbers')
        student.group_id = request.POST.get('group')

        if request.FILES.get('avatar'):
            student.avatar = request.FILES.get('avatar')

        student.save()
        return redirect('student_index')

    groups = Group.objects.all()
    return render(request, 'student_update.html', {
        'student': student,
        'groups': groups
    })

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_index')
    return render(request, 'student_delete.html', {
        'student': student
    })

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {
        'student': student
    })

# === Group ===

def group_index(request):
    query = request.GET.get('q', '')
    if query:
        groups = Group.objects.filter(name__icontains=query)
    else:
        groups = Group.objects.all()

    groups_count = groups.count()

    return render(
        request,
        'group_index.html',
        {'groups': groups, 'groups_count': groups_count},
    )

def group_detail(request, id):


    group = get_object_or_404(Group, id=id)
    
    students = group.student_set.all()

    return render(request, 'group_detail.html', {
        'group': group,
        'students': students
    })

def group_create(request):
    teachers = Teacher.objects.all()

    if request.method == "POST":
        messages.success(request, "Группа успешно создана!")
        return redirect("group_index")

    return render(request, "group_create.html", {"teachers": teachers})

def group_update(request, id):
    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':
        group.name = request.POST.get('name')
        group.start_date = request.POST.get('start_date')
        group.end_date = request.POST.get('end_date') or None
        group.course = request.POST.get('course')
        group.student_count = request.POST.get('student_count') or 0
        group.contract = request.POST.get('contract')
        
        mentor_id = request.POST.get('mentor')
        group.mentor_id = mentor_id if mentor_id else None

        group.save()
        return redirect('group_index')

    teachers = Teacher.objects.all()
    return render(request, 'group_update.html', {'group': group, 'teachers': teachers})

def group_delete(request, id):
    group = get_object_or_404(Group, id=id)
    
    if request.method == 'POST':
        group.delete()
        return redirect('group_index')
        
    return render(request, 'group_delete.html', {'group': group})

# === Teacher ===

def teacher_index(request):
    query = request.GET.get('q', '')
    if query:
        teachers = Teacher.objects.filter(name__icontains=query)
    else:
        teachers = Teacher.objects.all()

    teachers_count = teachers.count()

    return render(
        request,
        'teacher_index.html',
        {'teachers': teachers, 'teachers_count': teachers_count},
    )

def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    groups = teacher.groups.all() if hasattr(teacher, 'groups') else []
    return render(request, 'teacher_detail.html', {'teacher': teacher, 'groups': groups})

def teacher_create(request):
    groups = Group.objects.all()  

    if request.method == "POST":
        messages.success(request, "Преподаватель успешно добавлен!")
        return redirect("teacher_index")

    return render(request, "teacher_create.html", {"groups": groups})

def teacher_update(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        teacher.director = request.POST.get('director')
        teacher.name = request.POST.get('name')
        teacher.phone = request.POST.get('phone')
        teacher.experience = request.POST.get('experience') or 0
        teacher.save()
        return redirect('teacher_index')

    return render(request, 'teacher_update.html', {
        'teacher': teacher, 
        'choices': Teacher.DIRECTION_CHOICES
    })

def teacher_delete(request, id):

    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_index')
    
    return render(request, 'teacher_delete.html', {'teacher': teacher})

# === StudentMark ===

def mark_index(request):
    query = request.GET.get('q', '')
    if query:
        marks = StudentMark.objects.filter(
            Q(student__first_name__icontains=query) | Q(student__last_name__icontains=query)
        )
    else:
        marks = StudentMark.objects.all()

    return render(request, 'mark_index.html', {'marks': marks})

def mark_detail(request, id):
    mark = get_object_or_404(StudentMark, id=id)
    return render(request, 'mark_detail.html', {'mark': mark})

def mark_delete(request, id):

    mark = get_object_or_404(StudentMark, id=id)
    if request.method == 'POST':
        mark.delete()
        return redirect('mark_index')
    
    return render(request, 'mark_delete.html', {'mark': mark})

def mark_create(request):

    students = Student.objects.all() 
    teachers = Teacher.objects.all()

    if request.method == "POST":
        messages.success(request, "Оценка успешно поставлена!")
        return redirect("mark_index")

    return render(
        request,
        "mark_create.html",
        {"students": students, "teachers": teachers},
    ) 

def mark_update(request, id):
    mark = get_object_or_404(StudentMark, id=id)
    if request.method == 'POST':
        mark.student_id = request.POST.get('student')
        mark.mark = request.POST.get('mark')
        mark.save()
        return redirect('mark_index')

    students = Student.objects.all()
    return render(request, 'mark_update.html', {'mark': mark, 'students': students})