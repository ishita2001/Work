# Generated by Django 2.2.1 on 2019-07-01 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.Seller'),
        ),
    ]