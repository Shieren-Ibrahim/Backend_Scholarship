# Generated by Django 4.2.7 on 2023-12-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0013_university_sch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.IntegerField(choices=[(0, 'Accepted'), (1, 'Rejected'), (2, 'Under_consideration')], default=0),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='stage',
            field=models.CharField(choices=[('1', 'Bachalor'), ('2', 'Naster'), ('3', 'Doctoral')], max_length=20),
        ),
    ]