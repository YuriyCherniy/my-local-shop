# Generated by Django 2.2.10 on 2020-03-06 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0048_auto_20200306_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category_manager.Category', verbose_name='Категория товара'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]