# Generated by Django 3.2.7 on 2023-12-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allTrees', '0014_auto_20231220_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainstore_products',
            name='mainImage',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]