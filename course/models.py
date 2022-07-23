from django.db import models

# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, null=False)

    def __str__(self) -> str:
        return self.name

        #para não retornar <object NxNN> e sim o nome, caso exista

    class Meta:
        abstract = True

class Course(ModelBase):
    name = models.CharField(max_length=40, null=False)

    class Meta:
        db_table = 'course'
        managed = True

class Student(ModelBase):
    name = models.CharField(max_length=128, null=False)

    class Meta:
        db_table = 'student'
        managed = True

class StudentCourse(ModelBase):
    student = models.ForeignKey(
        to='Student',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_student'
    )
    course = models.ForeignKey(
        to='Course',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_course'
    )

    class Meta:
        db_table = 'student_course'
        managed = True
        unique_together = [('student', 'course')]