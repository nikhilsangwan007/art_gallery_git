# Generated by Django 3.1 on 2020-09-08 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art_gallery_app', '0009_auto_20200908_1129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paintings',
            new_name='Painting',
        ),
    ]