# Generated by Django 4.2.5 on 2023-10-02 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='date_order',
        ),
        migrations.AddField(
            model_name='order',
            name='date_delivery',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
