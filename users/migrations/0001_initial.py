# Generated by Django 3.2.6 on 2021-08-22 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('username', models.CharField(max_length=120)),
                ('is_verified', models.BooleanField(default=False)),
                ('auth_type', models.CharField(choices=[('EMAIL', 'EMAIL'), ('GITHUB', 'GITHUB')], default='EMAIL', max_length=120)),
                ('is_staff', models.BooleanField(default=False)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('is_superuser', models.BooleanField(default=False)),
                ('verification_token', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.verification')),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
    ]
