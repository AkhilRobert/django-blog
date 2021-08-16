# Generated by Django 3.2.6 on 2021-08-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('username', models.CharField(max_length=120)),
                ('is_verified', models.BooleanField(default=False)),
                ('auth_type', models.CharField(choices=[('EMAIL', 'EMAIL'), ('GITHUB', 'GITHUB')], default='EMAIL', max_length=120)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]