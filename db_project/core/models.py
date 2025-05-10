from django.db import models


class Classroom(models.Model):
    building = models.CharField(max_length=15) 
    room_number = models.CharField(max_length=7)
    capacity = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'classroom'
        constraints = [
            models.UniqueConstraint(
                fields=['building', 'room_number'], name='building_room_number'
            )
        ]
        
    def __str__(self):
        return f'{self.building} - {self.room_number}'


class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=20)
    building = models.CharField(max_length=15, blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'department'
        
    def __str__(self):
        return f'{self.dept_name}'


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    credits = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'course'
        
    def __str__(self):
        return f'{self.course_id}'
        

class Instructor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=5) 
    name = models.CharField(max_length=20)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'instructor'
        
    def __str__(self):
        return f'ID={self.id} - Name={self.name}'
        

class Section(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True)  
    sec_id = models.CharField(max_length=8, unique=True)
    semester = models.CharField(max_length=6)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    room_id = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='ID', to_field='id', related_name='section_room_number_set', blank=True, null=True)
    time_slot_id = models.ForeignKey('TimeSlot', models.DO_NOTHING, blank=True, null=True)

    class Meta: 
        db_table = 'section'
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'sec_id', 'semester', 'year'], name='course_sec_id_semester_year'
            )
        ]
        
    def __str__(self):
        return f'({self.course}) {self.year}-{self.semester}, classroom={self.room_id}, time slot={self.time_slot_id}'
        

class Teaches(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=4) 
    ins_id = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='ins_ID', to_field='id') 
    course = models.ForeignKey(Course, models.DO_NOTHING)
    sec = models.ForeignKey(Section, models.DO_NOTHING, db_column='sec_id', to_field='sec_id', related_name='teaches_sec_set')

    class Meta:
        db_table = 'teaches'
        constraints = [
            models.UniqueConstraint(
                fields=['id', 'course', 'sec'], name='teaches_id_course_sec'
            )
        ]
        
    def __str__(self):
        return f'{self.ins_id} - {self.course} - {self.sec}'
        

class Student(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=5) 
    name = models.CharField(max_length=20)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    tot_cred = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'student'
    
    def __str__(self):
        return f'ID={self.id} - Name={self.name}'


class Takes(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=4) 
    s_id = models.ForeignKey(Student, models.DO_NOTHING, db_column='s_ID', to_field='id') 
    course= models.ForeignKey(Course, models.DO_NOTHING)
    sec = models.ForeignKey(Section, models.DO_NOTHING, to_field='sec_id', related_name='takes_sec_set')
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'takes'
        constraints = [
            models.UniqueConstraint(
                fields=['id', 'course', 'sec'], name='takes_id_course'
            )
        ]
        
    def __str__(self):
        return f'student_id={self.s_id} - grade={self.grade}- {self.course}'
        
        
class Advisor(models.Model):
    s = models.OneToOneField('Student', models.DO_NOTHING, db_column='s_ID', primary_key=True)  
    i = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='i_ID', blank=True, null=True)  
    
    class Meta:
        db_table = 'advisor'


class TimeSlot(models.Model):
    time_slot_id = models.CharField(primary_key=True, max_length=4)
    day = models.CharField(max_length=1)
    start_hr = models.DecimalField(max_digits=2, decimal_places=0)
    start_min = models.DecimalField(max_digits=2, decimal_places=0)
    end_hr = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    end_min = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'time_slot'
        constraints = [
            models.UniqueConstraint(
                fields=['time_slot_id', 'day', 'start_hr', 'start_min'], name='time_slot_id_day_start_hr_start_min'
            )
        ]
        
    def __str__(self):
        return f'day={self.day} - {self.start_hr}:{self.start_min} to {self.end_hr}:{self.end_min}'
        
    
class Prereq(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True)  
    prereq = models.ForeignKey(Course, models.DO_NOTHING, related_name='prereq_prereq_set')

    class Meta:
        db_table = 'prereq'
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'prereq'], name='course_prereq'
            )
        ]

    def __str__(self):
        return f'{self.course} has prereq:{self.prereq}'


