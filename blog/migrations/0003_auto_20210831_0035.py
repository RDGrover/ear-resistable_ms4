# Generated by Django 3.2.6 on 2021-08-31 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_at']},
        ),
    ]
