# Generated by Django 5.1.6 on 2025-03-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_remove_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
