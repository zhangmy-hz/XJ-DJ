# Generated by Django 2.1.15 on 2020-07-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xunjie', '0022_so_first_api_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_del',
            name='item_gg',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
