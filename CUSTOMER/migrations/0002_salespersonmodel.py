# Generated by Django 4.1.3 on 2022-12-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CUSTOMER', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesPersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SAL_NAM_MDL', models.CharField(max_length=50)),
                ('SAL_ID_MDL', models.IntegerField()),
                ('SAL_BAS_MDL', models.CharField(choices=[('SOUTH_PATTAYA', 'SOUTH PATTAYA'), ('U-TAPAO', 'U-TAPAO')], max_length=25)),
            ],
            options={
                'verbose_name': 'SALESPERSON',
                'verbose_name_plural': 'SALESPERSON(s)',
            },
        ),
    ]
