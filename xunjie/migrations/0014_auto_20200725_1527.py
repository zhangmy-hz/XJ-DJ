# Generated by Django 2.1.15 on 2020-07-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xunjie', '0013_purchase_order_tou_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_order_tou',
            name='status',
            field=models.CharField(default='待下发', max_length=10, null=True),
        ),
    ]
