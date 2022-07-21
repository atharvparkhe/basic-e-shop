# Generated by Django 4.0.6 on 2022-07-14 13:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
                ('img', models.ImageField(upload_to='product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='activitymodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='serviceimages',
            name='service',
        ),
    ]