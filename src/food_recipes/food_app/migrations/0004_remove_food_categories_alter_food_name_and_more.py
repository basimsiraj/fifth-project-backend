# Generated by Django 5.0 on 2023-12-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0003_remove_food_category_food_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='categories',
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='food',
            name='publisher_name',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
