# Generated by Django 4.2.7 on 2023-12-22 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0012_alter_university_country_delete_university_sch'),
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
