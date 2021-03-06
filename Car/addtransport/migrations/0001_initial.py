# Generated by Django 3.1.6 on 2021-04-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/images')),
                ('price_tag', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
