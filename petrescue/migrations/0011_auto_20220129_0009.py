# Generated by Django 3.2.11 on 2022-01-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petrescue', '0010_auto_20220128_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='adopt_reason',
            field=models.TextField(blank=True, choices=[('Companion', 'Companion'), ('Guard_Dog', 'Guard_Dog'), ('Breeding', 'Breeding'), ('Other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='current_residence',
            field=models.TextField(blank=True, choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Condo', 'Condo')]),
        ),
    ]
