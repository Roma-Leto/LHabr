# Generated by Django 4.0 on 2024-04-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LHabrApp', '0005_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
