# Generated by Django 4.2.7 on 2023-12-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0003_country_country_scholarship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(null=True, upload_to='students_profiles'),
        ),
    ]