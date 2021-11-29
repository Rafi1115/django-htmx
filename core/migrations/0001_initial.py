# Generated by Django 3.2.8 on 2021-11-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('dute_date', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '1. Todo',
                'ordering': ['-name'],
            },
        ),
    ]