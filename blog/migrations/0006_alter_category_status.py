# Generated by Django 4.2 on 2024-08-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_comments_alter_comment_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
