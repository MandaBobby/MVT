# Generated by Django 5.0.7 on 2024-09-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=124)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
