from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

    # === Student ===


    path('student_index/', views.student_index, name='student_index'),
    path('student_detail/<int:id>', views.student_detail, name='student_detail'),
    path('student_create/', views.student_create, name='student_create'),
    path('student_update/<int:id>', views.student_update, name='student_update'),
    path('student_delete/<int:id>', views.student_delete, name = 'student_delete'),

    # === Group ===
    path('group_index/', views.group_index, name='group_index'),
    path('group_detail/<int:id>/', views.group_detail, name='group_detail'),
    path('group_create/', views.group_create, name='group_create'),
    path('group_update/<int:id>/', views.group_update, name='group_update'),
    path('group_delete/<int:id>/', views.group_delete, name='group_delete'),

    # === Teacher ===
    path('teacher_index/', views.teacher_index, name='teacher_index'),
    path('teacher_detail/<int:id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher_create/', views.teacher_create, name='teacher_create'),
    path('teacher_update/<int:id>/', views.teacher_update, name='teacher_update'),
    path('teacher_delete/<int:id>/', views.teacher_delete, name='teacher_delete'),
    
    # === StudentMark ===
    path('mark_index/', views.mark_index, name='mark_index'),
    path('mark_detail/<int:id>/', views.mark_detail, name='mark_detail'),
    path('mark_create/', views.mark_create, name='mark_create'),
    path('mark_update/<int:id>/', views.mark_update, name='mark_update'),
    path('mark_delete/<int:id>/', views.mark_delete, name='mark_delete'),

]
