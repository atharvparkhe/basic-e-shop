# Generated by Django 4.0.6 on 2022-07-14 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_productmodel_remove_activitymodel_category_and_more'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemsmodel',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_items', to='app.productmodel'),
        ),
    ]
