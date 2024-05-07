# Generated by Django 5.0.4 on 2024-05-07 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
    ]
