from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    
    # Student urls
    path("students/", views.StudentListView.as_view(), name="students"),
    path("student_detail/<str:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("student_delete/<str:pk>/", views.StudentDeleteView.as_view(), name="student_delete"),
    path("student_update/<str:pk>/", views.StudentUpdateView.as_view(), name="student_update"),
    path("student_create/", views.StudentCreateView.as_view(), name="student_create"),
    
    # Instructor urls
    path("instructors/", views.InstructorListView.as_view(), name="instructors"),
    path("instructor_detail/<str:pk>/", views.InstructorDetailView.as_view(), name="instructor_detail"),
    path("instructor_delete/<str:pk>/", views.InstructorDeleteView.as_view(), name="instructor_delete"),
    path("instructor_update/<str:pk>/", views.InstructorUpdateView.as_view(), name="instructor_update"),
    path("instructor_create/", views.InstructorCreateView.as_view(), name="instructor_create"),
    
    # Course urls
    path("courses/", views.CourseListView.as_view(), name="courses"),
    path("course_detail/<str:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
    path("course_delete/<str:pk>/", views.CourseDeleteView.as_view(), name="course_delete"),
    path("course_update/<str:pk>/", views.CourseUpdateView.as_view(), name="course_update"),
    path("course_create/", views.CourseCreateView.as_view(), name="course_create"),
    
    # Department urls    
    path("departments/", views.DepartmentListView.as_view(), name="departments"),
    path("department_detail/<str:pk>/", views.DepartmentDetailView.as_view(), name="department_detail"),
    path("department_delete/<str:pk>/", views.DepartmentDeleteView.as_view(), name="department_delete"),
    path("department_update/<str:pk>/", views.DepartmentUpdateView.as_view(), name="department_update"),
    path("department_create/", views.DepartmentCreateView.as_view(), name="department_create"),
    
    # Takes urls
    path("takes/", views.TakeListView.as_view(), name="takes"),
    path("take_detail/<str:pk>/", views.TakeDetailView.as_view(), name="take_detail"),
    path("take_delete/<str:pk>/", views.TakeDeleteView.as_view(), name="take_delete"),
    path("take_update/<str:pk>/", views.TakeUpdateView.as_view(), name="take_update"),
    path("take_create/", views.TakeCreateView.as_view(), name="take_create"),

    # Teaches urls
    path("teaches/", views.TeachListView.as_view(), name="teaches"),
    path("teach_detail/<str:pk>/", views.TeachDetailView.as_view(), name="teach_detail"),
    path("teach_delete/<str:pk>/", views.TeachDeleteView.as_view(), name="teach_delete"),
    path("teach_update/<str:pk>/", views.TeachUpdateView.as_view(), name="teach_update"),
    path("teach_create/", views.TeachCreateView.as_view(), name="teach_create"),
    
    # Section urls
    path("sections/", views.SectionListView.as_view(), name="sections"),
    path("section_detail/<str:pk>/", views.SectionDetailView.as_view(), name="section_detail"),
    path("section_delete/<str:pk>/", views.SectionDeleteView.as_view(), name="section_delete"),
    path("section_update/<str:pk>/", views.SectionUpdateView.as_view(), name="section_update"),
    path("section_create/", views.SectionCreateView.as_view(), name="section_create"),

    # Classroom urls
    path("classrooms/", views.ClassroomListView.as_view(), name="classrooms"),
    path("classroom_detail/<str:pk>/", views.ClassroomDetailView.as_view(), name="classroom_detail"),
    path("classroom_delete/<str:pk>/", views.ClassroomDeleteView.as_view(), name="classroom_delete"),
    path("classroom_update/<str:pk>/", views.ClassroomUpdateView.as_view(), name="classroom_update"),
    path("classroom_create/", views.ClassroomCreateView.as_view(), name="classroom_create"),
    
    # Advisor urls
    path("advisors/", views.AdvisorListView.as_view(), name="advisors"),
    path("advisor_detail/<str:pk>/", views.AdvisorDetailView.as_view(), name="advisor_detail"),
    path("advisor_delete/<str:pk>/", views.AdvisorDeleteView.as_view(), name="advisor_delete"),
    path("advisor_update/<str:pk>/", views.AdvisorUpdateView.as_view(), name="advisor_update"),
    path("advisor_create/", views.AdvisorCreateView.as_view(), name="advisor_create"),
    
    # Prereq urls
    path("prereqs/", views.PrereqListView.as_view(), name="prereqs"),
    path("prereq_detail/<str:pk>/", views.PrereqDetailView.as_view(), name="prereq_detail"),
    path("prereq_delete/<str:pk>/", views.PrereqDeleteView.as_view(), name="prereq_delete"),
    path("prereq_update/<str:pk>/", views.PrereqUpdateView.as_view(), name="prereq_update"),
    path("prereq_create/", views.PrereqCreateView.as_view(), name="prereq_create"),
    
    # Time slot urls
    path("time_slots/", views.TimeSlotListView.as_view(), name="time_slots"),
    path("time_slot_detail/<str:pk>/", views.TimeSlotDetailView.as_view(), name="time_slot_detail"),
    path("time_slot_delete/<str:pk>/", views.TimeSlotDeleteView.as_view(), name="time_slot_delete"),
    path("time_slot_update/<str:pk>/", views.TimeSlotUpdateView.as_view(), name="time_slot_update"),
    path("time_slot_create/", views.TimeSlotCreateView.as_view(), name="time_slot_create"),
]
