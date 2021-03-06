# Generated by Django 3.2.11 on 2022-01-28 23:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('petrescue', '0009_auto_20220127_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foster',
            name='ages_of_children',
        ),
        migrations.AddField(
            model_name='applicant',
            name='adopt_reason',
            field=models.TextField(blank=True, choices=[('Companion', 'Companion'), ('Guard_Dog', 'Guard_Dog'), ('Breeding', 'Breeding'), ('Other', 'Other')], default='companion'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='ages_children',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='current_residence',
            field=models.TextField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Condo', 'Condo')], default='house'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='date_updated',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='fenced_yard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicant',
            name='num_adults',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='applicant',
            name='num_children',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='applicant',
            name='other_pets',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicant',
            name='other_pets_desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='pet_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='petrescue.pet'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='primary_owner',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='applicant',
            name='vet_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='street_line_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='good_with_cats',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pet',
            name='good_with_dogs',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pet',
            name='good_with_kids',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pet',
            name='heart_worm_positive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Medium', max_length=15),
        ),
    ]
