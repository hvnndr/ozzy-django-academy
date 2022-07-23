# Generated by Django 4.0.6 on 2022-07-23 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_criando_modelo_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(db_column='id_course', on_delete=django.db.models.deletion.DO_NOTHING, to='course.course')),
                ('student', models.ForeignKey(db_column='id_student', on_delete=django.db.models.deletion.DO_NOTHING, to='course.student')),
            ],
            options={
                'db_table': 'student_course',
                'managed': True,
                'unique_together': {('student', 'course')},
            },
        ),
    ]