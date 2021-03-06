# Generated by Django 2.2.8 on 2020-06-19 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_project_essential_percent_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='essential_task_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='essential_percent_complete',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=20),
        ),
    ]
