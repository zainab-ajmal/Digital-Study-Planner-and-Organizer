# Generated by Django 5.1.3 on 2024-11-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_notebook_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='content',
        ),
        migrations.AddField(
            model_name='notebook',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]