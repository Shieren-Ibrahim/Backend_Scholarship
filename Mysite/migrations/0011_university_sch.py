# Generated by Django 4.2.7 on 2023-12-21 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0010_remove_rate_student_std_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='University_Sch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mysite.scholarship')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mysite.university')),
            ],
        ),
    ]