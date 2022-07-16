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
