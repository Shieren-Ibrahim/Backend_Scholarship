# Generated by Django 4.2.7 on 2023-12-21 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0011_university_sch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mysite.country'),
        ),
        migrations.DeleteModel(
            name='University_Sch',
        ),
    ]
