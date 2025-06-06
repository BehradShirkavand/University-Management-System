# Generated by Django 4.2.1 on 2023-06-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_course_credits'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='takes',
            name='takes_id_course_sec_semester_year',
        ),
        migrations.RemoveConstraint(
            model_name='teaches',
            name='teaches_id_course_sec_semester_year',
        ),
        migrations.RemoveField(
            model_name='takes',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='takes',
            name='year',
        ),
        migrations.RemoveField(
            model_name='teaches',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='teaches',
            name='year',
        ),
        migrations.AlterField(
            model_name='section',
            name='semester',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='section',
            name='year',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AddConstraint(
            model_name='takes',
            constraint=models.UniqueConstraint(fields=('id', 'course', 'sec'), name='takes_id_course'),
        ),
        migrations.AddConstraint(
            model_name='teaches',
            constraint=models.UniqueConstraint(fields=('id', 'course', 'sec'), name='teaches_id_course_sec'),
        ),
    ]
