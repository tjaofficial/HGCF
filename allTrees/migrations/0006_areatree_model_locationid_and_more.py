# Generated by Django 4.1.7 on 2023-04-04 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allTrees', '0005_alter_individualtrees_model_treeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='areatree_model',
            name='locationID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allTrees.locationtree_model'),
        ),
        migrations.AddField(
            model_name='individualtrees_model',
            name='areaID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allTrees.areatree_model'),
        ),
        migrations.AddField(
            model_name='individualtrees_model',
            name='locationID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allTrees.locationtree_model'),
        ),
    ]
