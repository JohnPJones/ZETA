# Generated by Django 4.1.3 on 2022-12-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInputModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CUS_CV_MDL', models.IntegerField()),
                ('CUS_NAM_MDL', models.CharField(max_length=60)),
                ('CUS_TYP_MDL', models.CharField(max_length=25)),
                ('BUS_NAM_MDL', models.CharField(max_length=50)),
                ('SAL_NAM_MDL', models.CharField(max_length=50)),
            ],
        ),
    ]
