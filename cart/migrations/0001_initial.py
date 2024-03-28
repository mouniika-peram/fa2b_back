# Generated by Django 5.0.3 on 2024-03-27 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('prd_title', models.CharField(max_length=100)),
                ('prd_img', models.ImageField(upload_to='')),
                ('prd_price', models.FloatField(default=0)),
                ('qty', models.FloatField(default=0)),
                ('net_amt', models.FloatField(default=0)),
                ('prd_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]