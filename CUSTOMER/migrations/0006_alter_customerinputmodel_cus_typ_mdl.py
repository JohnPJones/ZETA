# Generated by Django 4.1.3 on 2022-12-10 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CUSTOMER', '0005_alter_customerinputmodel_cus_typ_mdl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinputmodel',
            name='CUS_TYP_MDL',
            field=models.CharField(max_length=25),
        ),
    ]
