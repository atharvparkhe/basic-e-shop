# Generated by Django 4.0.6 on 2022-07-14 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_orderitemsmodel_item'),
        ('app', '0002_productmodel_remove_activitymodel_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActivityModel',
        ),
        migrations.DeleteModel(
            name='ServiceImages',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='app.categorymodel'),
        ),
    ]