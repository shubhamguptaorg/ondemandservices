# Generated by Django 2.0.3 on 2018-03-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulk_email_sender', '0002_email_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maildata_send_in_bulk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_data_send_in_bulk', models.CharField(max_length=50)),
                ('reciver_data_send_in_bulk', models.CharField(max_length=50)),
                ('subject_data_send_in_bulk', models.CharField(max_length=50)),
                ('message_data_send_in_bulk', models.CharField(max_length=100)),
            ],
        ),
    ]
