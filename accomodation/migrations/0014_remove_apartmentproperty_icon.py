# Generated by Django 4.1.3 on 2022-12-11 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0013_alter_apartmentproperty_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentproperty',
            name='icon',
        ),
    ]
