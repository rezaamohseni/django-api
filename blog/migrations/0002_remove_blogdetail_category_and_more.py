# Generated by Django 4.2 on 2024-08-10 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetail',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blogdetail',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='blogdetail',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='BlogDetail',
        ),
    ]
