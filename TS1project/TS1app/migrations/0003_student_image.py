# Generated by Django 4.2.3 on 2023-07-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TS1app', '0002_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
