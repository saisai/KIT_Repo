# Generated by Django 3.2.3 on 2021-07-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210705_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legacycontrolitem',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]