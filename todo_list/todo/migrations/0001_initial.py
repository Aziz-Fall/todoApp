# Generated by Django 3.0.7 on 2020-08-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50, verbose_name="task's name")),
                ('is_doing', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True, verbose_name="task's date")),
            ],
            options={
                'verbose_name': 'todo',
                'verbose_name_plural': 'todos',
                'ordering': ['date'],
            },
        ),
    ]
