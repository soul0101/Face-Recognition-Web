# Generated by Django 3.1.7 on 2021-03-20 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0004_auto_20210320_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_data', models.ImageField(blank=True, upload_to='Face Encodings')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.RemoveField(
            model_name='face',
            name='user',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.DeleteModel(
            name='Face',
        ),
    ]
