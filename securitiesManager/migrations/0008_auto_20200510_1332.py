# Generated by Django 3.0.6 on 2020-05-10 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securitiesManager', '0007_index_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_price',
            name='index',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='securitiesManager.Index'),
        ),
    ]
