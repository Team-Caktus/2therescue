# Generated by Django 3.2.11 on 2022-01-30 02:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('petrescue', '0011_auto_20220129_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='about_us',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='agency',
            name='agency_mission',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='agency',
            name='agency_owner',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='business_hours',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='agency',
            name='facebook',
            field=models.URLField(default=True, max_length=250),
        ),
        migrations.AddField(
            model_name='agency',
            name='instagram',
            field=models.URLField(default=True, max_length=250),
        ),
        migrations.AddField(
            model_name='agency',
            name='twitter',
            field=models.URLField(default=True, max_length=250),
        ),
        migrations.AddField(
            model_name='agency',
            name='website_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='foster_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='health_concerns',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='status',
            field=models.TextField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Denied', 'Denied'), ('Open', 'Open')], default=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='city',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='num_adults',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='num_children',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='pet_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='petrescue.pet'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='state',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='street_line_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='zipcode',
            field=models.IntegerField(blank=True, default=False),
        ),
    ]
