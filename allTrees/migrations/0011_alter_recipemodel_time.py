# Generated by Django 3.2.7 on 2023-12-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allTrees', '0010_alter_recipemodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='time',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
