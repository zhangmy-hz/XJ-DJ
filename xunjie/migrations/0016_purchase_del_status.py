# Generated by Django 2.1.15 on 2020-07-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xunjie', '0015_auto_20200726_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_del',
            name='status',
            field=models.CharField(default='待下发', max_length=10, null=True),
        ),
    ]
