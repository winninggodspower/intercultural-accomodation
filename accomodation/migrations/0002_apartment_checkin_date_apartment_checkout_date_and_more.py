# Generated by Django 4.1.3 on 2022-12-08 20:30

import accomodation.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='checkin_date',
            field=models.DateField(default=datetime.date(2022, 12, 8)),
        ),
        migrations.AddField(
            model_name='apartment',
            name='checkout_date',
            field=models.DateField(default=datetime.date(2022, 12, 8), validators=[accomodation.models.valid_checkout_date]),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]