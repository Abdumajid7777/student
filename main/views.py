from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Group, Teacher, StudentMark
def index(request):
    q = request.GET.get('q', '').strip()
    
    groups = Group.objects.all()

    if q:
        students = Student.objects.filter(
            Q(first_name__icontains=q) | Q(last_name__icontains=q)
        )
    else:
        students = Student.objects.all()

    return render(request, 'index.html', {
        'students': students,
        'groups': groups  
    })

def index(request):
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

def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age') or None
        phone_numbers = request.POST.get('phone_numbers')
        parent_phone_numbers = request.POST.get('parent_phone_numbers')
        group_id = request.POST.get('group')
        avatar = request.FILES.get('avatar')

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            phone_numbers=phone_numbers,
            parent_phone_numbers=parent_phone_numbers,
            group_id=group_id,
            avatar=avatar
        )
        return redirect('index')

    groups = Group.objects.all()
    return render(request, 'student_create.html', {'groups': groups})

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
        return redirect('index')

    groups = Group.objects.all()
    return render(request, 'student_update.html', {
        'student': student,
        'groups': groups
    })

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'student_delete.html', {
        'student': student
    })

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {
        'student': student
    })

# === Group ===

def group_detail(request, id):


    group = get_object_or_404(Group, id=id)
    
    students = group.student_set.all()

    return render(request, 'group_detail.html', {
        'group': group,
        'students': students
    })

def group_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date') or None
        course = request.POST.get('course')
        student_count = request.POST.get('student_count') or 0
        contract = request.POST.get('contract')
        mentor_id = request.POST.get('mentor')

        Group.objects.create(
            name=name,
            start_date=start_date,
            end_date=end_date,
            course=course,
            student_count=student_count,
            contract=contract,
            mentor_id=mentor_id if mentor_id else None
        )
        return redirect('index')

    teachers = Teacher.objects.all()
    return render(request, 'group_create.html', {'teachers': teachers})

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
        return redirect('index')

    teachers = Teacher.objects.all()
    return render(request, 'group_update.html', {'group': group, 'teachers': teachers})

def group_delete(request, id):
    group = get_object_or_404(Group, id=id)
    
    if request.method == 'POST':
        group.delete()
        return redirect('index')
        
    return render(request, 'group_delete.html', {'group': group})

# === Teacher ===

def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    groups = teacher.groups.all() if hasattr(teacher, 'groups') else []
    return render(request, 'teacher_detail.html', {'teacher': teacher, 'groups': groups})

def teacher_create(request):
    if request.method == 'POST':
        director = request.POST.get('director')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        experience = request.POST.get('experience') or 0

        Teacher.objects.create(
            director=director,
            name=name,
            phone=phone,
            experience=experience
        )
        return redirect('index')

    return render(request, 'teacher_create.html', {'choices': Teacher.DIRECTION_CHOICES})

def teacher_update(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        teacher.director = request.POST.get('director')
        teacher.name = request.POST.get('name')
        teacher.phone = request.POST.get('phone')
        teacher.experience = request.POST.get('experience') or 0
        teacher.save()
        return redirect('index')

    return render(request, 'teacher_update.html', {
        'teacher': teacher, 
        'choices': Teacher.DIRECTION_CHOICES
    })

def teacher_delete(request, id):

    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('index')
    
    return render(request, 'teacher_delete.html', {'teacher': teacher})

# === StudentMark ===

def mark_detail(request, id):
    mark = get_object_or_404(StudentMark, id=id)
    return render(request, 'mark_detail.html', {'mark': mark})

def mark_delete(request, id):

    mark = get_object_or_404(StudentMark, id=id)
    if request.method == 'POST':
        mark.delete()
        return redirect('index')
    
    return render(request, 'mark_delete.html', {'mark': mark})

def mark_create(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        mark_value = request.POST.get('mark')

        student = get_object_or_404(Student, id=student_id)
        StudentMark.objects.create(
            student=student,
            mark=mark_value
        )
        return redirect('index')

    students = Student.objects.all() 
    return render(request, 'mark_create.html', {'students': students})

def mark_update(request, id):
    mark = get_object_or_404(StudentMark, id=id)
    if request.method == 'POST':
        mark.student_id = request.POST.get('student')
        mark.mark = request.POST.get('mark')
        mark.save()
        return redirect('index')

    students = Student.objects.all()
    return render(request, 'mark_update.html', {'mark': mark, 'students': students})