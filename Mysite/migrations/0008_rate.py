# Generated by Django 4.2.7 on 2023-12-19 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0007_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.IntegerField()),
                ('two', models.IntegerField()),
                ('three', models.IntegerField()),
                ('four', models.IntegerField()),
                ('five', models.IntegerField()),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mysite.scholarship')),
            ],
        ),
    ]
