# Generated by Django 2.1.11 on 2020-09-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_aboutus_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='aboutimg/')),
            ],
        ),
    ]
