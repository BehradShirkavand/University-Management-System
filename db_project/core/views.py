from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from . import models


class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')


class StudentListView(ListView):
    model = models.Student
    template_name = 'core/student/student_list.html'
    
class StudentDetailView(DetailView):
    model = models.Student
    template_name = 'core/student/student_detail.html'

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy('core:students')
    template_name = 'core/student/student_confirm_delete.html'

class StudentUpdateView(UpdateView):
    model = models.Student
    fields = ['name', 'dept_name', 'tot_cred']
    template_name = "core/student/student_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:student_detail', kwargs={'pk':self.kwargs['pk']})

class StudentCreateView(CreateView):
    model = models.Student
    fields = '__all__'
    template_name = "core/student/student_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:student_detail', kwargs={'pk':self.object.pk}) 
    
    
class InstructorListView(ListView):
    model = models.Instructor
    template_name = 'core/instructor/instructor_list.html'
    
class InstructorDetailView(DetailView):
    model = models.Instructor
    template_name = 'core/instructor/instructor_detail.html'

class InstructorDeleteView(DeleteView):
    model = models.Instructor
    success_url = reverse_lazy('core:instructors')
    template_name = 'core/instructor/instructor_confirm_delete.html'

class InstructorUpdateView(UpdateView):
    model = models.Instructor
    fields = ['name', 'dept_name', 'salary']
    template_name = "core/instructor/instructor_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:instructor_detail', kwargs={'pk':self.kwargs['pk']})

class InstructorCreateView(CreateView):
    model = models.Instructor
    fields = '__all__'
    template_name = "core/instructor/instructor_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:instructor_detail', kwargs={'pk':self.object.pk}) 
    
    
class CourseListView(ListView):
    model = models.Course
    template_name = 'core/course/course_list.html'
    
class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'core/course/course_detail.html'

class CourseDeleteView(DeleteView):
    model = models.Course
    success_url = reverse_lazy('core:courses')
    template_name = 'core/course/course_confirm_delete.html'

class CourseUpdateView(UpdateView):
    model = models.Course
    fields = ['title', 'dept_name', 'credits']
    template_name = "core/course/course_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:course_detail', kwargs={'pk':self.kwargs['pk']})

class CourseCreateView(CreateView):
    model = models.Course
    fields = '__all__'
    template_name = "core/course/course_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:course_detail', kwargs={'pk':self.object.pk}) 


class DepartmentListView(ListView):
    model = models.Department
    template_name = 'core/department/department_list.html'
    
class DepartmentDetailView(DetailView):
    model = models.Department
    template_name = 'core/department/department_detail.html'

class DepartmentDeleteView(DeleteView):
    model = models.Department
    success_url = reverse_lazy('core:departments')
    template_name = 'core/department/department_confirm_delete.html'

class DepartmentUpdateView(UpdateView):
    model = models.Department
    fields = ['dept_name', 'building', 'budget']
    template_name = "core/department/department_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:department_detail', kwargs={'pk':self.kwargs['pk']})

class DepartmentCreateView(CreateView):
    model = models.Department
    fields = '__all__'
    template_name = "core/department/department_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:department_detail', kwargs={'pk':self.object.pk}) 
       
    
class TakeListView(ListView):
    model = models.Takes
    template_name = 'core/take/take_list.html'
    
class TakeDetailView(DetailView):
    model = models.Takes
    template_name = 'core/take/take_detail.html'

class TakeDeleteView(DeleteView):
    model = models.Takes
    success_url = reverse_lazy('core:takes')
    template_name = 'core/take/take_confirm_delete.html'

class TakeUpdateView(UpdateView):
    model = models.Takes
    fields = ['s_id', 'course', 'sec', 'grade']
    template_name = "core/take/take_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:take_detail', kwargs={'pk':self.kwargs['pk']})

class TakeCreateView(CreateView):
    model = models.Takes
    fields = '__all__'
    template_name = "core/take/take_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:take_detail', kwargs={'pk':self.object.pk})
    

class TeachListView(ListView):
    model = models.Teaches
    template_name = 'core/teach/teach_list.html'
    
class TeachDetailView(DetailView):
    model = models.Teaches
    template_name = 'core/teach/teach_detail.html'

class TeachDeleteView(DeleteView):
    model = models.Teaches
    success_url = reverse_lazy('core:teaches')
    template_name = 'core/teach/teach_confirm_delete.html'

class TeachUpdateView(UpdateView):
    model = models.Teaches
    fields = ['ins_id', 'course', 'sec']
    template_name = "core/teach/teach_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:teach_detail', kwargs={'pk':self.kwargs['pk']})

class TeachCreateView(CreateView):
    model = models.Teaches
    fields = '__all__'
    template_name = "core/teach/teach_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:teach_detail', kwargs={'pk':self.object.pk})
           

class SectionListView(ListView):
    model = models.Section
    template_name = 'core/section/section_list.html'
    
class SectionDetailView(DetailView):
    model = models.Section
    template_name = 'core/section/section_detail.html'

class SectionDeleteView(DeleteView):
    model = models.Section
    success_url = reverse_lazy('core:sections')
    template_name = 'core/section/section_confirm_delete.html'

class SectionUpdateView(UpdateView):
    model = models.Section
    fields = ['course', 'year', 'semester', 'room_id', 'time_slot_id']
    template_name = "core/section/section_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:section_detail', kwargs={'pk':self.kwargs['pk']})

class SectionCreateView(CreateView):
    model = models.Section
    fields = '__all__'
    template_name = "core/section/section_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:section_detail', kwargs={'pk':self.object.pk})
    

class ClassroomListView(ListView):
    model = models.Classroom
    template_name = 'core/classroom/classroom_list.html'
    
class ClassroomDetailView(DetailView):
    model = models.Classroom
    template_name = 'core/classroom/classroom_detail.html'

class ClassroomDeleteView(DeleteView):
    model = models.Classroom
    success_url = reverse_lazy('core:classrooms')
    template_name = 'core/classroom/classroom_confirm_delete.html'

class ClassroomUpdateView(UpdateView):
    model = models.Classroom
    fields = ['building', 'room_number', 'capacity']
    template_name = "core/classroom/classroom_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:classroom_detail', kwargs={'pk':self.kwargs['pk']})

class ClassroomCreateView(CreateView):
    model = models.Classroom
    fields = '__all__'
    template_name = "core/classroom/classroom_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:classroom_detail', kwargs={'pk':self.object.pk})
    

class AdvisorListView(ListView):
    model = models.Advisor
    template_name = 'core/advisor/advisor_list.html'
    
class AdvisorDetailView(DetailView):
    model = models.Advisor
    template_name = 'core/advisor/advisor_detail.html'

class AdvisorDeleteView(DeleteView):
    model = models.Advisor
    success_url = reverse_lazy('core:advisors')
    template_name = 'core/advisor/advisor_confirm_delete.html'

class AdvisorUpdateView(UpdateView):
    model = models.Advisor
    fields = ['s', 'i']
    template_name = "core/advisor/advisor_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:advisor_detail', kwargs={'pk':self.kwargs['pk']})

class AdvisorCreateView(CreateView):
    model = models.Advisor
    fields = '__all__'
    template_name = "core/advisor/advisor_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:advisor_detail', kwargs={'pk':self.object.pk})  
    

class PrereqListView(ListView):
    model = models.Prereq
    template_name = 'core/prereq/prereq_list.html'
    
class PrereqDetailView(DetailView):
    model = models.Prereq
    template_name = 'core/prereq/prereq_detail.html'

class PrereqDeleteView(DeleteView):
    model = models.Prereq
    success_url = reverse_lazy('core:prereqs')
    template_name = 'core/prereq/prereq_confirm_delete.html'

class PrereqUpdateView(UpdateView):
    model = models.Prereq
    fields = ['course', 'prereq']
    template_name = "core/prereq/prereq_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:prereq_detail', kwargs={'pk':self.kwargs['pk']})

class PrereqCreateView(CreateView):
    model = models.Prereq
    fields = '__all__'
    template_name = "core/prereq/prereq_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:prereq_detail', kwargs={'pk':self.object.pk})
    
    
class TimeSlotListView(ListView):
    model = models.TimeSlot
    template_name = 'core/time_slot/time_slot_list.html'
    
class TimeSlotDetailView(DetailView):
    model = models.TimeSlot
    template_name = 'core/time_slot/time_slot_detail.html'

class TimeSlotDeleteView(DeleteView):
    model = models.TimeSlot
    success_url = reverse_lazy('core:time_slots')
    template_name = 'core/time_slot/time_slot_confirm_delete.html'

class TimeSlotUpdateView(UpdateView):
    model = models.TimeSlot
    fields = ['day', 'start_hr', 'start_min', 'end_hr', 'end_min']
    template_name = "core/time_slot/time_slot_update_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:time_slot_detail', kwargs={'pk':self.kwargs['pk']})

class TimeSlotCreateView(CreateView):    
    model = models.TimeSlot
    fields = '__all__'
    template_name = "core/time_slot/time_slot_create_form.html"
    
    def get_success_url(self):
        return reverse_lazy('core:time_slot_detail', kwargs={'pk':self.object.pk})

     