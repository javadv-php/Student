# Generated by Django 3.2.7 on 2021-09-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_student_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user_type',
            field=models.BooleanField(default=True),
        ),
    ]
