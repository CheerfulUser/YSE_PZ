# Generated by Django 2.0.4 on 2019-12-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0048_transient_context_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquery',
            name='python_query',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
