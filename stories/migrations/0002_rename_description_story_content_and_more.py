# Generated by Django 5.1.6 on 2025-03-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='story',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.CharField(default='Unknown Author', max_length=100),
        ),
        migrations.AlterField(
            model_name='story',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
