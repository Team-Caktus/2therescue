# Generated by Django 3.2.11 on 2022-01-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petrescue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('num_of_adults', models.IntegerField()),
                ('ages_of_children', models.CharField(max_length=50)),
                ('any_other_pets', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='image_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
