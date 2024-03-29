# Generated by Django 3.2.7 on 2023-12-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allTrees', '0012_mainstore_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainstore_products',
            name='shipping_weight',
            field=models.FloatField(default=0.00),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainstore_products',
            name='track_inventory',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='inventory_status',
            field=models.CharField(blank=True, choices=[('in_stock', 'In stock'), ('out_of_stock', 'Out of stock')], max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='inventory_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='limit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='limit_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='pre_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='pre_order_message',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='sale_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='sale_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainstore_products',
            name='show_in_store',
            field=models.BooleanField(default=True),
        ),
    ]
