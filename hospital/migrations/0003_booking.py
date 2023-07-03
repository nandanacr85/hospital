# Generated by Django 4.1.4 on 2023-06-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_email', models.EmailField(max_length=254)),
                ('p_phone', models.CharField(max_length=100)),
                ('doc_name', models.CharField(max_length=100)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
