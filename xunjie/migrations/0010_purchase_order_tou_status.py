# Generated by Django 2.1.15 on 2020-07-24 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xunjie', '0009_purchase_del'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order_tou',
            name='status',
            field=models.CharField(default='未审核', max_length=10, null=True),
        ),
    ]
