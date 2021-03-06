# Generated by Django 2.2.1 on 2020-07-24 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WashingMachine',
            fields=[
                ('washing_machine_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('washing_machine_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_slot_date', models.DateField()),
                ('user_slot_start_time', models.TimeField()),
                ('user_slot_end_time', models.TimeField()),
                ('user_slot_status', models.CharField(choices=[('BOOKED', 'BOOKED'), ('NOTBOOKED', 'NOTBOOKED')], max_length=100)),
                ('slot_username', models.CharField(max_length=40)),
                ('washing_machine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slot_booking.WashingMachine')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_day', models.CharField(choices=[('SUNDAY', 'SUNDAY'), ('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY'), ('SATURDAY', 'SATURDAY')], max_length=100)),
                ('slot_start_time', models.TimeField()),
                ('slot_end_time', models.TimeField()),
                ('washing_machine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slot_booking.WashingMachine')),
            ],
        ),
    ]
