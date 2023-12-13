# Generated by Django 5.0 on 2023-12-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('publisher_name', models.CharField(max_length=255)),
                ('featured_image', models.ImageField(upload_to='foods/images')),
                ('ingredients', models.TextField()),
                ('description', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
