# Generated by Django 4.2.3 on 2023-07-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
