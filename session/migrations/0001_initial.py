# Generated by Django 3.2.5 on 2021-07-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session_det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('datee', models.CharField(max_length=30)),
                ('timee', models.CharField(max_length=10)),
            ],
        ),
    ]
