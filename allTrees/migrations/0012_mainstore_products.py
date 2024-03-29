# Generated by Django 3.2.7 on 2023-12-20 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allTrees', '0011_alter_recipemodel_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainStore_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('ribbon', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=2000)),
                ('price', models.FloatField()),
                ('on_sale', models.BooleanField()),
                ('sale_percentage', models.IntegerField()),
                ('sale_price', models.FloatField()),
                ('inventory_status', models.BooleanField()),
                ('inventory_total', models.IntegerField()),
                ('pre_order', models.BooleanField()),
                ('pre_order_message', models.CharField(max_length=150)),
                ('limit', models.BooleanField()),
                ('limit_number', models.IntegerField()),
                ('show_in_store', models.BooleanField()),
                ('mainImage', models.ImageField(upload_to='')),
            ],
        ),
    ]
