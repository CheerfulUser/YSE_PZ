# Generated by Django 2.0.5 on 2018-09-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0021_auto_20180518_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='photometricband',
            name='disp_color',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
