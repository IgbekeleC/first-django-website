# Generated by Django 4.0.4 on 2022-05-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdboard', '0003_video_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
