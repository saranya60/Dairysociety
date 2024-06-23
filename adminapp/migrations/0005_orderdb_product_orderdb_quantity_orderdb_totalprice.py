# Generated by Django 5.0.6 on 2024-06-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_registerdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdb',
            name='Product',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderdb',
            name='Quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderdb',
            name='Totalprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]