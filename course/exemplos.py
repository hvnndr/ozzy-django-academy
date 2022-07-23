from course import models

# EXEMPLO 1 - Dada uma lista de alunos, cadastrar todos os alunos no mesmo curso.
def cadastra_alunos_1():
    curso = models.Course.objects.first()
    alunos = ['Jao', 'Vanilton', 'Ozzy', 'Barbosa', 'Caetano']

    for a in alunos:
        aluno = models.Student()
        aluno.name = a
        aluno.course = curso
        aluno.save()

def cadastra_alunos_2():
    curso = models.Course.objects.last()
    alunos = ['Hev', 'Cris', 'Rezende', 'Breno', 'Vini']

    for a in alunos:
        models.Student.objects.create(name=a, course=curso)


def cadastra_somente_alunos():
    alunos = ['Hev', 'Cris', 'Rezende', 'Breno', 'Vini']
    for a in alunos:
        aluno = models.Student()
        aluno.name = a
        aluno.save()

def associa_todos_cursos_a_todos_alunos():
    students = models.Student.objects.all()
    course = models.Course.objects.all()

    for s in students:
        for c in course:
            cs = models.StudentCourse()
            cs.student = s
            cs.course = c
            cs.save()
    
def consulta_students_by_course():
    course = models.Course.objects.first()
    list = course.students.all()
    print(list)    
    for l in list:
        print(l)

def consulta_course_by_students():
    student = models.Student.objects.first()
    list = student.courses.all()
    print(list)
    for l in list:
        print(l)