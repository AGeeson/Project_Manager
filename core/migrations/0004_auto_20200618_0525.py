# Generated by Django 2.2.8 on 2020-06-18 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200609_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='progress',
            field=models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('To Verify', 'To Verify'), ('Bugged', 'Bugged'), ('Completed', 'Completed')], default='To Do', max_length=30),
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('task_progress', models.CharField(max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='core.Task')),
            ],
        ),
    ]
