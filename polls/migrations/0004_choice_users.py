# Generated by Django 4.2.11 on 2024-04-23 15:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_alter_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
